# Dataframes - Operations

import numpy as np
import pandas as pd


df = pd.DataFrame({'col1':[1,2,3,4],
                    'col2':[444,555,666,444],
                    'col3':['abc', 'def', 'ghi', 'xyz']})


df.head()


# Finding unique values
df['col2'].unique()

# Returning number of unique values
df['col2'].nunique()

# How many times each unique value appears
df['col2'].value_counts()

# Selecting data

df[df['col1']>2]

# Apply method is one of the most powerful in pandas
# apply() is used to apply functions to dataframes
def times2(x):
    return x*2

df['col1'].apply(times2)

df['col3'].apply(len)

df['col2'].apply(lambda x: x*2)


df.drop('col1', axis=1)

# grab column index names

df.columns

df


df.sort_values(by='col2')


# returns a dataframe of booleans where the values are null
df.isnull()

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],s
        'C':['x','y','x','y','x','y',],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

df

# Pivot Tables

df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
