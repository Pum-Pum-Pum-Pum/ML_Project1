import yaml
from housing.exception import HousingException
import os,sys

def read_yaml_file(filepath:str)->dict:
    """

    Args:
        filepath (str): Reads the yaml file from the file path provided

    Returns:
        dict: return the yaml file contents as a dictionary
    """
    try:
        with open(filepath,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        return HousingException(e,sys) from e
        