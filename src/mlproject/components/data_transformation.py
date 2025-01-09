import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import MinMaxScaler

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def dropcolumn(self):
        data=pd.read_csv(self.config.data_path)
        data=data.drop("Serial No.", axis=1)

        return data

    def MinMaxScaler(self):
        data = self.dropcolumn()
        scaler = MinMaxScaler(feature_range=(0, 1))
        data["GRE Score"] = scaler.fit_transform(data[["GRE Score"]])
        data["TOEFL Score"] = scaler.fit_transform(data[["TOEFL Score"]])

        return data


    def train_test_spliting(self):
        data = self.MinMaxScaler()

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)