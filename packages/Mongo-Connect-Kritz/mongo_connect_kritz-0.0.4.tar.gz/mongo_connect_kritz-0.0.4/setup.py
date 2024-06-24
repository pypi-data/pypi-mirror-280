from setuptools import setup, find_packages  # setup tools here is the package and we are importing two modules from it or functions 
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME= "Mongo-Connect-Kritz" # This package name will be displayed on PyPI repository
AUTHOR_USER_NAME = "KrithikaVerma"
AUTHOR_EMAIL = "krithika.verma@gmail.com"

# Here to providing and giving details about your package    
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )



