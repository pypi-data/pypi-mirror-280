from pydantic import BaseModel, BeforeValidator, Field, ConfigDict, AliasGenerator, AliasChoices
from typing import Annotated, Union
from itertools import chain


"""
incoming_aliases define the changes needed from the incoming data item, keys to
the values created in the Pydantic data model
"""
incoming_aliases = {
    "additional_codes": AliasChoices("useAdditionalCode",
                                     "additional_codes"),
    "description": AliasChoices("desc", "description"),
    "inclusion_term": AliasChoices("inclusionTerm", "inclusion_term"),
    "code_first": AliasChoices("codeFirst", "code_first"),

}


def notes(value: Union[str, list, dict]) -> Union[list, str]:
    """
    Recursively flatten a nested list of strings or dictionaries containing "note" key.

    :param value: The input value to flatten.
    :type value: list or str or dict

    :return: A list of notes.
    :rtype: list

    :raises ValueError: If "note" key is not found in the expected field.

    """
    if isinstance(value, list):
        return list(chain(*[notes(v) for v in value]))
    elif isinstance(value, str):
        return [value]
    elif isinstance(value, dict):
        if "note" not in value.keys():
            raise ValueError("No notes found in the expected field")
        obj_notes = value["note"]
        if isinstance(obj_notes, str):
            return [obj_notes]
        else:
            return obj_notes


class Diagnosis(BaseModel):
    """
    Pydantic data model for Diagnosis.

    :param name: The name of the diagnosis.
    :type name: str
    :param description: The description of the diagnosis.
    :type description: str
    :param inclusion_term: The list of inclusion terms for the diagnosis. Defaults to an empty list.
    :type inclusion_term: list or None
    :param excludes1: The list of first-level exclusions for the diagnosis. Defaults to an empty list.
    :type excludes1: list or None
    :param excludes2: The list of second-level exclusions for the diagnosis. Defaults to an empty list.
    :type excludes2: list or None
    :param includes: The list of additional included diagnoses for the diagnosis. Defaults to an empty list.
    :type includes: list or None
    :param code_first: The list of codes that need to be mentioned first for the diagnosis. Defaults to an empty list.
    :type code_first: list or None
    :param additional_codes: The list of additional codes for the diagnosis. Defaults to an empty list.
    :type additional_codes: list or None
    :param parent: The parent of the diagnosis. Defaults to None.
    :type parent: str or None
    :param section_name: The name of the section that the diagnosis belongs to. Defaults to None.
    :type section_name: str or None
    :param section_description: The description of the section that the diagnosis belongs to. Defaults to None.
    :type section_description: str or None
    :param chapter: The chapter that the diagnosis belongs to. Defaults to None.
    :type chapter: str or None
    """
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: incoming_aliases.get(field_name, None)
        )
    )
    name: str
    description: str
    inclusion_term: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    excludes1: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    excludes2: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    includes: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    code_first: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    additional_codes: Annotated[Annotated[list, BeforeValidator(notes)] | None, Field(default_factory=list)]
    parent: Annotated[str | None, Field(default_factory=None)]
    section_name: Annotated[str | None, Field(default_factory=None)]
    section_description: Annotated[str | None, Field(default_factory=None)]
    chapter: Annotated[str | None, Field(default_factory=None)]
