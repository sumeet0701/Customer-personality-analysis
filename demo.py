from cpa.exception.exception_handler import CpaException
from cpa.logger.log import logging 
from cpa.components.data_ingestion import DataIngestion
from cpa.components.data_validation import DataValidation
from cpa.components.data_transformation import DataTransformation
from cpa.components.model_training import ModelTrainer
from cpa.pipeline.training_pipeline import TrainingPipeline


obj = DataIngestion()
obj.initiate_data_ingestion()
print("Data Ingestion Completed!")


obj = DataValidation()
obj.initiate_data_validation()
print("Data Ingestion Completed!")

obj = DataTransformation()
obj.initiate_data_transformation()
print("Data Validation Completed!")


obj = ModelTrainer()
obj.initiate_model_trainer()
print("Model Training Completed!")

obj = TrainingPipeline()
obj.start_training_pipeline()
print(" Training Completed!")