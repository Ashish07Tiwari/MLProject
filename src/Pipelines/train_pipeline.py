from src.Components.data_ingestion import DataIngestion
from src.Components.data_transformation import DataTransformer
from src.Components.model_trainer import ModelTrain

data_ingestion_obj = DataIngestion()
train_data_path, test_data_path= data_ingestion_obj.initiate_data_ingestion()

data_transformation_obj = DataTransformer()
train_data_arr, test_data_arr, _ = data_transformation_obj.initiate_data_transformer(train_data_path, test_data_path)

model_trainer_obj= ModelTrain()
print(model_trainer_obj.initiate_model_trainer(train_data_arr, test_data_arr))