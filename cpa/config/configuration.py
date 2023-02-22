import os,sys
from cpa.logger.log import logging
from cpa.exception.exception_handler import CpaException
from cpa.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig,ModelPredictionConfig,ModelTrainerConfig
from cpa.constant import *
from cpa.utils.utils import read_yaml_file

class CpaConfiguration:

    def __init__(self,config_file_path:str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise CpaException(e,sys)
        
    
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        try:
            data_ingestion_config = self.configs_info['data_ingestion_config']
            artfacts_dir = self.configs_info['artifact_config']['artifact_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir =os.path.join(artfacts_dir,dataset_dir,data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artfacts_dir,dataset_dir,data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url=data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f' Data Ingestion config: {response}')
            return response
        except Exception as e:
            raise CpaException(e, sys) from e
    

    # data validation 
    def get_data_validation_config(self)-> DataValidationConfig:
        try:
            data_validation_config = self.configs_info['data_validation_config']
            data_ingestion_config = self.configs_info['data_ingestion_config']
            dataset_dir = self.configs_info['dataset_dir']
            artifacts_dir = self.configs_info['artifact_dir']
            marketing_campaign_csv_file = data_validation_config['marketing_campaign_csv_file']

            marketing_campaign_csv_file_dir = os.path.join(artifacts_dir,dataset_dir,data_ingestion_config['ingested_dir'], marketing_campaign_csv_file)

            clean_data_path = os.path.join(artifacts_dir, dataset_dir,data_validation_config['clean_data_dir'])
            serialized_object_dir = os.path.join(artifacts_dir,data_ingestion_config['serialized_object_dir'])

            response = DataValidationConfig(
                clean_data_dir=clean_data_path,
                marketing_campaign_csv_file=marketing_campaign_csv_file_dir,
                serialized_objects_dir=serialized_object_dir
            )

            logging.info(f"Data Validation config: {response}")
            return response

        except Exception as e:
            raise CpaException(e,sys) from e

    
    # data transformation 

    def get_data_transformation_config(self)-> DataTransformationConfig:
        try:
            data_transformation_dir = self.configs_info['Data_transformation_dir']
            data_validation_dir = self.configs_info['data_validation_dir']
            data_ingestion_dir = self.configs_info['data_ingestion_dir']

            dataset_dir = self.configs_info['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_dir']

            clean_data_file_path = os.path.join(artifacts_dir,dataset_dir,data_validation_dir['clean_data_dir'],"clean_data.csv")
            transformed_data_file = os.path.join(artifacts_dir,dataset_dir,data_transformation_dir['transformed_data_dir'])

            response = DataTransformationConfig(
                clean_data_file_path=clean_data_file_path,
                transformed_data_dir=transformed_data_file

            )
            logging.info(f"Data Transformation Config: {response}")
            return response


        except Exception as e:
            raise CpaException(e,sys) from e

 # model Training :
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        try:

            model_trainer_config = self.configs_info['model_trainer_config']
            data_transformation_dir = self.configs_info['data_transformation_dir']
            data_validation_dir = self.configs_info['data_validation_dir']
            data_ingesetion_dir = self.configs_info['data_ingestion_dir']

            dataset_dir = self.configs_info['dataset_dir']
            artifacts_dir = self.configs_info['artifacts_dir']

            transformed_data_file = os.path.join(artifacts_dir,dataset_dir,data_transformation_dir['transformed_data_dir'],"transformed_data.csv")
            trained_model_dir = os.path.join(artifacts_dir,dataset_dir,model_trainer_config['trained_model_dir'])
            trained_model_name = model_trainer_config['trained_model_name']

            response = ModelTrainerConfig(
                transformed_data_file_dir=transformed_data_file,
                trained_model_dir=trained_model_dir,
                trained_model_name=trained_model_name
            )

            logging.info(f"Model Trainer Config: {response}")
            return response

        except Exception as e:
            raise CpaException(e, sys) from e

    # training pipeline:

    def get_prediction_config(self)-> ModelPredictionConfig:
        try:
            model_trainer_config = self.configs_info['model_trainer_config']
            trained_model_name = model_trainer_config['trained_model_name']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            trained_model_dir = os.path.join(artifacts_dir, model_trainer_config['trained_model_dir'])
            
            trained_model_path = os.path.join(trained_model_dir,trained_model_name)
          
            response = ModelPredictionConfig(
                trained_model_path = trained_model_path
            )

            logging.info(f"Model Prediction Config: {response}")
            return response

        except Exception as e:
            raise CpaException(e, sys) from e

