from tinydb import TinyDB, Query
import pathlib


class DrugsDatabase:

    def __init__(self, db_path: pathlib.Path) -> None:
        self.db = TinyDB(pathlib.Path(db_path, 'ndc_db.json'))
        self.generic_name_index = TinyDB(pathlib.Path(db_path, 'ndc_generic_name_index.json'))
        self.medication_class_index = TinyDB(pathlib.Path(db_path, 'ndc_medication_class_index.json'))
        self.ingredient_index = TinyDB(pathlib.Path(db_path, "ndc_ingredient_index.json"))
        self.ndc_index = TinyDB(pathlib.Path(db_path, "ndc_code_index.json"))

    def get_by_package_ndc(self, package_ndc: str):
        """
        :param package_ndc: The package NDC (National Drug Code) to search for, in string format.
        :return: Returns the corresponding database record, if found. Otherwise, it returns None.
        """
        q = Query()
        product_codes = package_ndc.split("-")
        if len(product_codes) > 1:
            record_id = self.ndc_index.get(q.name == product_codes[0])["records"][product_codes[1]]
            return self.db.get(doc_id=record_id)
        return None

    def get_by_class(self, medication_class: str):
        """
        :param medication_class: The class of medication to search for.
        :return: The medication records matching the specified class.
        """
        q = Query()
        index_recs = self.medication_class_index.search(q.name.matches(medication_class))
        return self.__get_recs__(index_recs)

    def get_by_generic_name(self, generic_name):
        """
        Get records by generic name.

        :param generic_name: The generic name to search for.
        :return: The records matching the generic name.
        """
        q = Query()
        index_recs = self.generic_name_index.search(q.name.matches(generic_name))
        return self.__get_recs__(index_recs)

    def get_by_ingredient(self, ingredient):
        """
        Fetches records based on the specified ingredient.

        :param ingredient: The ingredient to search for.
        :type ingredient: str
        :return: The records that match the specified ingredient.
        :rtype: list
        """
        q = Query()
        index_recs = self.ingredient_index.search(q.name.matches(ingredient))
        return self.__get_recs__(index_recs)

    def __get_recs__(self, index_recs):
        """
        :param index_recs: A list of dictionaries containing records.
        :return: A list of documents retrieved from the database based on the given record ids.
        """
        all_recs = []
        for recs in index_recs:
            all_recs.extend(recs["records"])
        return self.db.get(doc_ids=all_recs)

    def get_all_generic_names(self):
        """
        Get a list of all generic names.

        :return: A list of all generic names as strings.
        """
        return [x["name"] for x in self.generic_name_index.all()]

    def get_all_medication_classes(self):
        """
        Get a list of all medication classes.

        :return: List of medication class names.
        """
        return [x["name"] for x in self.medication_class_index.all()]

    def get_all_ingredients(self):
        """
        Get all the names of all ingredients.

        :return: A list of ingredient names.
        :rtype: list
        """
        return [x["name"] for x in self.ingredient_index.all()]



