from setuptools import setup, find_packages
from typing import List
    
# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.1"
AUTHOR="Pum-Pum-Pum-Pum"
DESCRIPTION="Lets beat Phil dunphy and become the best realtor"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Returns:
        A list with name of libraries from requirements.txt
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readline()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #PACKAGES,
    install_requires=get_requirements_list()
)
