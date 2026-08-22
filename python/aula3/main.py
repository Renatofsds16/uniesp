import pandas as pd
from time import sleep
url = 'https://raw.githubusercontent.com/nisston/disciplinaestruturadedados/main/datatran2021_Completa.csv'

sleep(1)
dataframe = pd.read_csv(url,encoding='latin-1',sep=';')
print(dataframe.shape)
print(dataframe.columns)
print(dataframe.info)
dataframe.isnull().sum()
dataframe.dropna(inplace=True, axis=0)
listaq1 = dataframe['municipio'].to_list()
listaq1[-5:]
for item in listaq1:
    print(item)
