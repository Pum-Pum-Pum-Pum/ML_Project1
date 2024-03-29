from housing.entity.config_entity import DataIngestionConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:
    
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise HousingException(e,sys)
    def download_housing_data(self)->str:
        try:
            # Extracting remote URL to download dataset
            download_url = self.data_ingestion_config.dataset_download_url
            
            # folder location to download the file
            tgz_download_file = self.data_ingestion_config.tgz_download_dir
            housing_file_name = os.path.basename(download_url)
            tgz_file_path = os.path.join(tgz_download_file, housing_file_name)
            # Checking if the path exists, if not it will be created
            if os.path.exists(tgz_file_path):
                os.remove(tgz_file_path)
            os.makedirs(tgz_file_path, exist_ok=True)
            logging.info(f"Downloading the data from [{download_url}] into the file path [{tgz_file_path}]")
            # to download the file
            urllib.request.urlretrieve(download_url, tgz_file_path)
            logging.info(f"File has been downloaded successfully in the path {tgz_file_path}")
            # Returning the file path where the data ia downloaded
            return tgz_file_path
        except Exception as e:
            raise HousingException(e,sys) from e
    def extract_tgz_file(self, tgz_file_path : str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            os.makedirs(raw_data_dir, exist_ok=True)
            
            logging.info(f"extracting tgz file and loading the raw data into [{raw_data_dir}]")
            # Opening the tgz file and loading the raw data into raw_data_dir
            with tarfile.open(tgz_file_path) as housing_tar_file_obj:
                housing_tar_file_obj.extractall(path=raw_data_dir)
            logging.info("Extraction of tgz file completed")
            
        except Exception as e:
            raise HousingException(e,sys) from e
    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            file_name = os.listdir(raw_data_dir)[0]
            housing_file_path = os.path.join(raw_data_dir, file_name)
            housing_data_frame = pd.read_csv(housing_file_path)
            
            # now lets split the data
            housing_data_frame["income_cat"] = pd.cut(
                housing_data_frame["median_income"],
                bins=[0.0, 1.5, 3.0 , 4.5, 6, np.inf],
                labels = [1, 2, 3, 4, 5]
            )
            
            # stratified split we have to do, without losing all the combos
            strat_train_set = None
            strat_test_set = None
            
            split = StratifiedShuffleSplit(n_splits=1, test_size= 0.2, random_state= 42)
            
            for train_index, test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]):
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"], axis = 1)
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"], axis = 1)
                
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)
            
            
        except Exception as e:
            raise HousingException(e,sys) from e
        
            
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
        except:
            raise HousingException(e,sys)
        