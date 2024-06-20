# pyDrugsDatabase

PyDrugsDatabase downloads the FDA drugs database so that it can be used locally. The database is also
indexed allowing for obtaining drugs by generic name, active ingredients and drug classes

## Tutorials

### Installation

To Install PyDrugDatabase from PyPI,

```shell
pip install pydrusgdatabase
```

### Loading the Database

To create and load the database, from the latest data, from the fda,

```python
import pathlib
from pydrugsdatabase.drugs_load import DrugsLoad

DrugsLoad(pathlib.Path("/path/to/save/db")).load_from_fda()
```
This will download, extract format and save the records, plus create a series of indexes to access the
records faster.


### Reading the Database

```python
import pathlib
from pydrugsdatabase.drugs_database import DrugsDatabase

drugs_db = DrugsDatabase(pathlib.Path("/path/to/db/"))
```

#### Obtaining records by Product or Package NDC

```python
rec = drugs_db.get_by_package_ndc("4444-333")
```

A single TinyDB Document object is returned. This is a modified Dictionary

!!! Note
    Records are stored by product NDC numbers. not package. The first two sets of number
    represent the product NDC id, and the last is used for the exact packaging. Drug details
    are the same for all packages (including dose), except for the size of the 
    package (number of doses)

#### Obtaining Records by Medication Class

Each Drug has multiple medication classes, representing different aspects
of the given drug, such as chemical class, main usage, chemical route used etc.
Some medications that have multiple active ingredients will have classes assigned
for each of the active ingredients used.

```python
recs = drugs_db.get_by_class("ssri")
```

A list of TinyDB Documents are returned

#### Obtaining Records By generic Name

```python
recs = drugs_db.get_by_generic_name("paracetamol")
```
A list of TinyDB Document objects is returned

#### Obtaining Records By Ingredient

The database holds lists of the active ingredients in a given medication, which
can be multiple, for example Adderall.

```python
recs = drugs_db.get_by_ingredient("paracetamol")
```

Returns a list of TinyDB Documents


#### Get all Generic Names

```python
names = drugs_db.get_all_generic_names()
```
returns a list of strings

#### get All Medication Classes

```python
class_names = drugs_db.get_all_medication_classes()
```

#### Get All Ingredients

```python
ingredients = drugs_db.get_all_ingredients()
```

returns a list of strings

### Accessing the Database directly

The Database and the indexes can be accessed directly. They
are all TinyDB instances

* obj.db: The main DB
* obj.ndc_index: Two layered index for the NDC product Id
* obj.generic_name_index:  Index of Generic names
* obj.medication_class_index: Index of Medication classes
* obj.ingredient_index: index of the Active ingredients

## Reference

Records in the database are stored in the following format.

* package_ndc: List of strings
* product_ndc: string
* generic_name: string (lowercase)
* brand_name: string (lowercase)
* active_ingredients: list of strings (lowercase)
* pharm_class: list of strings (lowercase)
* pharm_class_epc: list of strings (lowercase)
* pharm_class_cs: list of strings (lowercase)
* pharm_class_moa: list of strings (lowercase)
* pharm_class_pe: list of strings (lowercase)

There is also a calculated field called all_classes() that returns all class fields in one (no duplicates)


## Concepts

The FDA drugs database comes in a large json file format, with a lot of additional data. I have stripped away the 
majority of it, leaving the main classification elements, brand name, generic name, ingredients and medication classes.
the data is pulled and ran through a pydantic model to ensure standards before being saved.

The data is saved in tinyDB, thus no need to have a database server in place, just run the download and start
accessing the data

