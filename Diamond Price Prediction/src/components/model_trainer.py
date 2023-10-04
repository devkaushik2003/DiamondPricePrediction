from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sys,os
from dataclasses import dataclass
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

# Data Transormation config
class datatransformationconfig():
    preprocessor_ob_file_path = os.path.join('artifacts','preprocessor.pkl')

class datatransformation:
    def __init__(self):
        self.data_transformation_config = datatransformation()

    def get_data_transformation_object(self):
        try:
        

    def initate_data_transformation(self,tain_data_path,test_data_path):



