## this is entirly dedicated to transforming the data

from data_injection import data_injection
from src.logger import logging
import pandas as pd

get_injected_data = data_injection()
logging.info('getting the train and test set path')
train_path , test_path = get_injected_data.data_injection_start()

train_df = pd.read_csv(train_path)
print(train_df.head())





# if __name__ == '__main__':


