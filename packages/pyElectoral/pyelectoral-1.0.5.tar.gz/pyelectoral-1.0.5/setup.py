#  -*- coding: utf-8 -*-
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.5'
PACKAGE_NAME = "pyElectoral"
AUTHOR = "Robert Pérez"
AUTHOR_EMAIL = "delfinmundo@gmail.com"
URL = "https://rep98.vzlaweb.com"

LICENSE = "MIT"
DESCRIPTION = "Libreria Python para consultas al CNE de Venezuela con GUI integradas"
LONG_DESCRIPTION: str = (HERE / "README.md").read_text(encoding="utf-8")
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES: list[str] = [
    "requests",
    "bs4"
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = LONG_DESC_TYPE,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    install_requires= INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data = True
)