from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pydrugsdatabase',
    version='0.1.0',
    url='https://gitlab.com/marcnealer/pydrugsdatabase',
    author='Marc Nealer',
    author_email='marcnealer@gmail.com',
    description='Downloads the FDA drugs database along with the NDC codes active ingredients and drug classes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pydantic',
        'tinydb',
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)
