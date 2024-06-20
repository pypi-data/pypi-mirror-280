import datetime
import zipfile
import io
import pathlib
from tinydb import TinyDB
import xmltodict
import requests
from python_icd10.icd10_model import Diagnosis


class ICD10Load:

    def __init__(self, warehouse_path: pathlib.Path):
        """
        Initializes ICD10Load object.

        Initialization also clears any current data and will create the warehouse if it does not exist.

        :param warehouse_path: The path to where to store the ICD10 data. Must be a pathlib.Path object.
        """
        warehouse_path.mkdir(parents=True, exist_ok=True)
        self.db = TinyDB(pathlib.Path(warehouse_path, "icd10_warehouse.json"))
        self.base_url = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM"
        self.year = None
        self.db.truncate()
        self.diagnoses = []

    def load_from_cdc(self):
        """
        Load data from CDC (Centers for Disease Control and Prevention) by retrieving the latest file,
        extracting fom the zip, and parsing XML data to create ICD10 diagnoses records,
        which are then saved to the database

        :return: None
        """
        zip_in_memory = self.__get_latest_file()
        file_name = f"icd10cm-tabular-{self.year}.xml"
        with zipfile.ZipFile(zip_in_memory, 'r') as zip_ref:
            if file_name not in zip_ref.namelist():
                raise Exception(f"File {file_name} was not found in the downloaded zip")
            extracted_file = zip_ref.read(file_name)
        del zip_in_memory
        try:
            data = xmltodict.parse(extracted_file.decode("utf-8"))
        except ValueError as e:
            raise ValueError(f"Failed to parse XML from {extracted_file} {e.__str__()}")
        except AttributeError as e:
            raise AttributeError(f"Failed to parse XML from {extracted_file} {e.__str__()}")
        del extracted_file
        self.__extract_records(data)
        self.db.insert_multiple(self.diagnoses)

    def __get_latest_dir(self):
        """
        Get the latest ICD10CM data folder directory. The data is stored in files with the year
        as part of the path

        :return: The latest ICD10CM data folder directory.
        :rtype: str
        :raises Exception: If the latest ICD10CM data folder cannot be found.
        """
        self.year = datetime.datetime.now().year
        url = f"{self.base_url}/{self.year}"
        resp = requests.get(url)
        if not resp.ok:
            self.year = self.year - 1
            url = f"{self.base_url}/{self.year}"
            resp = requests.get(url)
            if not resp.ok:
                raise Exception("Failed to find the latest ICD10CM data folder")
        return

    def __get_latest_file(self):
        """
        Gets the latest file from cdc and holds it in memory

        :return: The Latest ICD10 data zip file as an in memory file.
        """
        self.__get_latest_dir()
        file_name = f"icd10cm-Table and Index-{self.year}.zip"
        url = f"{self.base_url}/{self.year}/{file_name}"
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
        memory_file = io.BytesIO(resp.content)
        memory_file.seek(0)
        return memory_file

    def __extract_records(self, data):
        """
        Extracts ICD10 data from the xml

        :param data: ICD10 data from the XML file converted to a dictionary.
        :return: None
        """
        chapters = data['ICD10CM.tabular']['chapter']
        if isinstance(chapters, list):
            for chapter in chapters:
                sections = chapter['section']
                chapter_name = chapter['name']
                if isinstance(sections, list):
                    for section in sections:
                        section_name = section['@id']
                        section_desc = section['desc']
                        if "diag" in section.keys():
                            self.extract_diags(section_name, section_desc,
                                               chapter_name, section["diag"], parent=None)
                else:
                    section_name = sections["@id"]
                    section_desc = sections["desc"]
                    if "diag" in sections.keys():
                        self.extract_diags(section_name, section_desc,
                                           chapter_name, sections["diag"], parent=None)

    def extract_diags(self, section_name, section_desc, chapter_name, diag, parent=None):
        """
        Extracts diagnoses to be stored in the database.

        This method is recursive as lists of diagnoses/codes can be found inside other lists.
        It also passes the section details, chapter and the parent ICD10 diagnoses code, if there
        is one.

        The diagnosis data is passed to a Pydantic Diagnosis model to be cleaned and prepped before
        its added to the record list

        :param section_name: Name of the section.
        :param section_desc: Description of the section.
        :param chapter_name: Name of the chapter.
        :param diag: Diagnosis information or a list of diagnosis information.
        :param parent: Parent diagnosis name (optional).
        :return: None
        """
        if isinstance(diag, list):
            [self.extract_diags(section_name, section_desc, chapter_name, x, parent=parent) for x in diag]
        else:
            self.diagnoses.append(Diagnosis(section_name=section_name,
                                            section_description=section_desc,
                                            chapter=chapter_name,
                                            parent=parent, **diag).model_dump())
            if "diag" in diag.keys():
                self.extract_diags(section_name=section_name, section_desc=section_desc,
                                   chapter_name=chapter_name, diag=diag["diag"], parent=diag["name"])
