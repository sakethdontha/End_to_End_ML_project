import pandas as pd
import os
from mlproject import logger
from sklearn.ensemble import GradientBoostingRegressor
import joblib
from mlproject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        train_data.columns=train_data.columns.str.strip()
        test_data.columns=test_data.columns.str.strip()

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        lr = GradientBoostingRegressor(n_estimators=self.config.n_estimators, learning_rate=self.config.learning_rate, max_depth=self.config.max_depth)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))