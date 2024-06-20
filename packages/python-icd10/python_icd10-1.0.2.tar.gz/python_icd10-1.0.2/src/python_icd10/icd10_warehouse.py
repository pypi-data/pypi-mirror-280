from tinydb import TinyDB, Query
from tinydb.table import Document
import re
import pathlib
from typing import List


class ICD10Warehouse:
    """
    ICD10Warehouse

    A class for reading the ICD-10 warehouse.

    """
    def __init__(self, warehouse_path: pathlib.Path):
        """
        Initialize the class creating a link to the ICD-10 warehouse.

        If the data has not be loaded, then a blank warehouse will be created.

        :param warehouse_path: Path to the warehouse location.
        :type warehouse_path: pathlib.Path
        """
        warehouse_path.mkdir(parents=True, exist_ok=True)
        self.db = TinyDB(pathlib.Path(warehouse_path, "icd10_warehouse.json"))

    def search_by_description(self, search_term: str) -> List[Document]:
        """
        Search the description field in the database for a given search term.

        :param search_term: The term to search for in the description field.
        :return: The results of the search query.
        """
        q = Query()
        return self.db.search(q.description.matches(search_term, re.IGNORECASE))

    def search_by_code(self, code: str) -> List[Document]:
        """
        :param code: The code used to search for documents.
        :return: A list of Document objects that match the given code.
        """
        q = Query()
        return self.db.search(q.name.matches(code, re.IGNORECASE))

    def get_by_code(self, code: str) -> Document:
        """
        Fetches a document from the database by code.

        :param code: The code of the document to retrieve.
        :type code: str
        :return: The document with the specified code, or None if not found.
        :rtype: Document
        """
        q = Query()
        return self.db.get(q.name == code)

    def get_all_codes(self) -> List[str]:
        """
        Retrieve all codes from the database.

        :return: A list of strings representing the code names.
        """
        return [x["name"] for x in self.db]

