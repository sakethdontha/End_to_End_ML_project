import os
import sys
import logging


logging_str= "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"

log_filepath=os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok=True)



logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # it created a foler name logs and file name running_log.log and stores msg in there
        logging.StreamHandler(sys.stdout)  # it gives the output in the terminal
    ]
)

logger=logging.getLogger("mlprojectlogger") #logger object called in main.py