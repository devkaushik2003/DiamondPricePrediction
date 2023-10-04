import os
import sys
import src.logger import logging
import src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# intialize the data ingestion configuration

@dataclass
class dataingestionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')


class dataingestion:
    def __init__(self):
        self.ingestion_config = dataingestionconfig()

    def intiate_data_ingestion(self):
        logging.info("data ingestion method start")

        try:
            df = pd.read_csv('notebook/data','gemstone.csv')
            logging.info("data set read as data frame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path)

            logging.info("Train test split")

            train_set , test_set = train_test_split(df,test_size=0.33,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            
            logging.info("ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("error occured in Data ingestion config")

    
