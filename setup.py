from setuptools import setup, find_packages
from typing import List
    
# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
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
        # remove("-e .") is added as packages=find_packages() will take care of all the files inside housing folder
        requirements = [line.strip() for line in requirements_file if "-e ." not in line]
        return requirements

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #PACKAGES,
    install_requires=get_requirements_list()
)
