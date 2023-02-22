import sys
from cpa.components.data_ingestion import DataIngestion
from cpa.components.data_validation import DataValidation
from cpa.components.data_transformation import DataTransformation
from cpa.components.model_training import ModelTrainer
from cpa.exception.exception_handler import CpaException

class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion = DataIngestion()
            self.data_validation = DataValidation()
            self.data_transformation = DataTransformation()
            self.model_trainer = ModelTrainer()
        except Exception as e:
            raise CpaException(e, sys) from e
     

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        try:
            self.data_ingestion.initiate_data_ingestion()
            self.data_validation.initiate_data_validation()
            self.data_transformation.initiate_data_transformation()
            self.model_trainer.initiate_model_trainer()
        except Exception as e:
            raise CpaException(e, sys) from e