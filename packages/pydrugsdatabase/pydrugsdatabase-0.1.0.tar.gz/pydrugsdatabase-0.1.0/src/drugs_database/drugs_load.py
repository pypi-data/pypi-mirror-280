import json
import pathlib

import requests
import zipfile
import io
import re
from pydantic import BaseModel, computed_field, Field, BeforeValidator
from typing import Annotated
from tinydb import TinyDB


def make_lower(value):
    return value.lower()


def make_list_lower(value):
    return [v.lower() for v in value]


def make_ingredients_lower(values):
    return_value = []
    for value in values:
        new_dict = {}
        for k, v in value.items():
            new_dict[k] = make_lower(v)
        return_value.append(new_dict)
    return return_value


class DrugsModel(BaseModel):
    package_ndc: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default=None)]
    product_ndc: Annotated[Annotated[str, BeforeValidator(make_lower)] | None, Field(defaul=None)]
    generic_name: Annotated[Annotated[str, BeforeValidator(make_lower)] | None, Field(default=None)]
    brand_name: Annotated[Annotated[str, BeforeValidator(make_lower)] | None, Field(default=None)]
    active_ingredients: Annotated[Annotated[list, BeforeValidator(make_ingredients_lower)] | None,
                                  Field(default_factory=list)]
    pharm_class: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default_factory=list)]
    pharm_class_epc: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default_factory=list)]
    pharm_class_cs: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default_factory=list)]
    pharm_class_moa: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default_factory=list)]
    pharm_class_pe: Annotated[Annotated[list, BeforeValidator(make_list_lower)] | None, Field(default_factory=list)]

    @computed_field
    def all_classes(self) -> list:
        return list(
            set(self.pharm_class + self.pharm_class_epc +
                self.pharm_class_cs + self.pharm_class_moa +
                self.pharm_class_pe))


class DrugsLoad:
    def __init__(self, db_path: pathlib.Path):
        db_path.mkdir(exist_ok=True, parents=True)
        self.url = "https://download.open.fda.gov/drug/ndc/drug-ndc-0001-of-0001.json.zip"
        self.db = TinyDB(pathlib.Path(db_path, 'drugs_db.json'))
        self.generic_name_index = TinyDB(pathlib.Path(db_path, 'drugs_generic_name_index.json'))
        self.medication_class_index = TinyDB(pathlib.Path(db_path, 'drugs_medication_class_index.json'))
        self.ingredient_index = TinyDB(pathlib.Path(db_path, "drugs_ingredient_index.json"))
        self.ndc_index = TinyDB(pathlib.Path(db_path, "drugs_code_index.json"))
        self.substring_index = TinyDB(pathlib.Path(db_path, "drugs_substring_index.json"))

    def load_from_fda(self):
        """
        Loads data from the FDA by extracting the latest file, extracting its content, and processing the data.

        :return: None
        """
        self.__extract_data(self.__extract_file(self.__get_latest_file()))

    def __get_latest_file(self):
        """
        Retrieves the latest file from the given URL.

        :return: A BytesIO object containing the content of the latest file.
        """
        resp = requests.get(self.url)
        resp.raise_for_status()
        return io.BytesIO(resp.content)

    @staticmethod
    def __extract_file(file_obj):
        """
        Extracts the contents of a Zip file and returns the data contained in the "results" field of the extracted JSON file.

        :param file_obj: The file object representing the Zip file.
        :return: The contents of the "results" field from the extracted JSON file.
        """
        with zipfile.ZipFile(file_obj) as zip_ref:
            f = zip_ref.open(zip_ref.namelist()[0])
            data = json.load(f)
            return data["results"]

    def __extract_data(self, results):
        """
        :param results: A list of dictionaries containing the extracted data from the source
        :return: None

        This method is responsible for extracting data from the provided 'results' and inserting it into the database. It performs the following steps:
        1. Truncates the existing data in the database.
        2. Initializes an empty list 'items' to store the extracted records.
        3. Iterates through each 'result' in the 'results' list.
        4. Extracts the package_ndc value from each result's packaging.
        5. Constructs a DrugsModel object with the package_ndc and other fields from the result.
        6. Appends the resulting model's dump (serializable representation) to the 'items' list.
        7. Inserts multiple items in the 'items' list into the database.
        8. Calls the private methods '__create_ndc_index', '__create_generic_index', '__create_medication_class_index', and '__create_ingredient_index' to create indexes in the database.
        """
        self.db.truncate()
        items = []
        for result in results:
            package_ndc = [v["package_ndc"] for v in result["packaging"]]
            rec = DrugsModel(package_ndc=package_ndc, **result)
            items.append(rec.model_dump())
        self.db.insert_multiple(items)
        self.__create_ndc_index()
        self.__create_generic_index()
        self.__create_medication_class_index()
        self.__create_ingredient_index()

    def __create_generic_index(self):
        """
        Create a generic name index based on the documents in the database.

        :return: None
        """
        self.generic_name_index.truncate()
        generic_index = {}
        for doc in self.db.all():
            if doc["generic_name"]:
                names = re.split(",|\sand\s", doc["generic_name"])
                for name in names:
                    nm = name.strip()
                    if nm not in generic_index:
                        generic_index[nm] = [doc.doc_id]
                    else:
                        generic_index[nm].append(doc.doc_id)
        self.generic_name_index.insert_multiple([{"name": k, "records": v} for k, v in generic_index.items()])

    def __create_medication_class_index(self):
        """
        Create a medication class index by iterating through all the documents in the database.
        Each document contains a list of medication classes.
        This method creates a dictionary where the keys are medication classes and the values are lists
        of document IDs that contain that medication class.
        Finally, the method inserts the medication class index into the `medication_class_index` collection.

        :return: None
        """
        self.medication_class_index.truncate()
        medication_class_index = {}
        for doc in self.db.all():
            for med_class in doc["all_classes"]:
                mcls = re.split(",|\sand\s", med_class)
                for cls in mcls:
                    ccls = cls.strip()
                    if ccls not in medication_class_index:
                        medication_class_index[ccls] = [doc.doc_id]
                    else:
                        medication_class_index[ccls].append(doc.doc_id)
        self.medication_class_index.insert_multiple([{"name": k, "records": v} for k, v in medication_class_index.items()])

    def __create_ingredient_index(self):
        """
        Create an index of ingredients in the database.

        Truncates the current ingredient index. Then iterates through all documents in the database.
        For each document, iterates through the active ingredients and populates the ingredient index.

        :return: None
        """
        self.ingredient_index.truncate()
        ingredient_index = {}
        for doc in self.db.all():
            for ingredient in doc["active_ingredients"]:
                if ingredient["name"] not in ingredient_index:
                    ingredient_index[ingredient["name"]] = [doc.doc_id]
                else:
                    ingredient_index[ingredient["name"]].append(doc.doc_id)
        self.ingredient_index.insert_multiple([{"name": k, "records": v} for k, v in ingredient_index.items()])

    def __create_ndc_index(self):
        """
        Create an NDC index based on the product_ndc field in the database.

        :return: None
        """
        self.ndc_index.truncate()
        ndc_index = {}
        for doc in self.db.all():
            product1, product2 = doc["product_ndc"].split("-")
            if product1 not in ndc_index:
                ndc_index[product1] = {product2: doc.doc_id}
            else:
                ndc_index[product1][product2] = doc.doc_id
        self.ndc_index.insert_multiple([{"name": k, "records": v} for k, v in ndc_index.items()])

