## this file is reponsiable for reading the files and changing them for trainng and testing
import os
import sys
from src.logger import logging
from src.exception import customeException
import pandas as pd
from sklearn.model_selection import train_test_split

class injection_configue:
    def __init__(self):
        self.train_path: str = os.path.join('artifact','train.csv')
        self.test_path : str = os.path.join('artifact','test.csv')
        self.raw_path : str = os.path.join('artifact','raw.csv')
    
class data_injection():
    def __init__(self):
        self.path = injection_configue()
    def data_injection_start(self):
        try:
            df1 = pd.read_csv('notebooks\\Datasets\\data\\test.csv')
            df2 = pd.read_csv('notebooks\\Datasets\\data\\train.csv')
            df = pd.concat([df1,df2],axis=1)
            logging.info('Raw Data store started')

            os.makedirs(os.path.dirname(self.path.raw_path),exist_ok=True)
            df.to_csv(self.path.raw_path,index=False,header=True)

            logging.info('Raw data store ends here')
            logging.info(5*'-')
            logging.info('Train_test Slipt Started')

            y = df['Survived']
            train_set , test_set = train_test_split(df,stratify=y,random_state=56,train_size=0.8)

            logging.info('training and test data store started')
            #os.path.dirname: 
            #'/path/to/some/file.txt', and the value of directory will be 
            #'/path/to/some'. 
            # It effectively removes the last component of the path (in this case, the file name)
            # and returns the directory containing that file.

            os.makedirs(os.path.dirname(self.path.train_path),exist_ok=True)
            train_set.to_csv(self.path.train_path,index=False,header=True)
            os.makedirs(os.path.dirname(self.path.test_path),exist_ok=True)
            test_set.to_csv(self.path.test_path,index=False,header=True)

            logging.info('training and test data store ended')
            
        except Exception as e:
            logging.info(customeException(e.__str__(),sys).__str__())
            raise customeException(e.__str__(),sys)



# if __name__ == '__main__':
#     data_injection = data_injection()
#     data_injection.data_injection_start()
