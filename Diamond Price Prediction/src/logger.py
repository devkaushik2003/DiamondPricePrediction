import logging
import os
from datetime import datetime

LOG_FILE  = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # this creates a log file which has date time month and year in it
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE) # this will create a log path folder 
os.makedirs(logs_path,exist_ok=True) # this will create the log folder and exist_ok checks if the folder already exists then it will leave no changes will be made

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename='LOG_FILE_PATH',
    format="[ %(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
#in the end its just basic logging with filename and format and level
