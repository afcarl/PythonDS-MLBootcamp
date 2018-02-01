#!/usr/bin/python3
import seaborn as sns
import numpy as np
import pandas as pd

path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Pandas Built-in Data Viz/'

df1 = pd.read_csv(path +'df1', index_col=0)
df2 = pd.read_csv(path + 'df2')

# .hist() actually calls matplotlib, so you can use most matplotlib args
df1['A'].hist(bins=30)

df1['A'].plot(kind='hist', bins=30)

df1['A'].plot.hist()


df2.plot.area(alpha=0.4)

df2.plot.bar()

df1['A'].plot.hist(bins=50)
df1.plot.line(x=df1.index, y='B', figsize=(12,3), lw=1)

# c is setting the color of the plot.

df1.plot.scatter(x='A', y='B', c='C', cmap='plasma')
