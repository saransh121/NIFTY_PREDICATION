import logging
import os
from datetime import datetime

file_date = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.curdir,'LOGS',file_date)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,file_date)

logging.basicConfig(
     filename=LOG_FILE_PATH,
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
 )

# if __name__ == '__main__':
#     logging.info('logging has started')


