from housing.entity.config_entity import DataIngestionConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
from six.moves import urllib

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
            os.makedirs(tgz_file_path, exist_ok=True)
            logging.info(f"Downloading the data from [{download_url}] into the file path [{tgz_file_path}]")
            # to download the file
            urllib.request.urlretrieve(download_url, tgz_file_path)
            logging.info(f"File has been downloaded successfully in the path {tgz_file_path}")
            # Returning the file path where the data ia downloaded
            return tgz_file_path
        except Exception as e:
            raise HousingException(e,sys) from e
    def extract_tgz_file(self):
        pass
    def split_data_as_train_test(self):
        pass
            
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()
            
        except:
            raise HousingException(e,sys)
        