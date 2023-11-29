from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransfomationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
import os
from housing.constant import *



ROOT_DIR = os.getcwd()


class Configuration:
    def __init__(self, config_file_path = CONFIG_FILE_PATH)->None:
        pass
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass
    def get_data_validation_config(self) -> DataValidationConfig:
        pass
    def get_data_transformation_config(self) -> DataTransfomationConfig:
        pass
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass
    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        pass
        