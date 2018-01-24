# Input & Output - CSV, Excel, SQL, & HTML
import numpy as np
import pandas as pd
import os


path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/'

### CSV INPUT ###
df = pd.read_csv(path + 'example.csv')
df

df.to_csv(path + 'My_output', index=False)
pd.read_csv('My_output')

# Pandas can only import data


### EXCEL INPUT ###
pd.read_excel(path + 'Excel_Sample.xlsx', sheet_name='Sheet1')
df.to_excel(path + 'Excel_Sample2.xlsx', sheet_name='TestSheet')

### HTML INPUT ### Pandas searches for <table></table> and extropolates the data into a list
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


type(data)

data[0].head()


### SQL INPUT ### Not very good because of the vast DB options

from  sqlalchemy import create_engine
# creating a dummy db engine
engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)

sqldf
