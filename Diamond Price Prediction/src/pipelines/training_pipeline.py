import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import dataingestion

if __name__ == "__main__":
    obj = dataingestion()
    train_data_path , test_data_path = obj.intiate_data_ingestion()
    print(train_data_path,test_data_path)