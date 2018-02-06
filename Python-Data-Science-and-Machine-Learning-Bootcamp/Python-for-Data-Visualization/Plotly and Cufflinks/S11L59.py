#!/usr/bin/python3
import pandas as pd
import numpy as np
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
%matplotlib inline

# DATA
df = pd.DataFrame(np.random.randn(100,4), columns= 'A B C D'.split())
df.head()
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values':[32,43,50]})

df2.head()

# iplot() is plotly magic, makes the plot very interactive
df.iplot()

# Using iplot to create other plot types

# plotly tries to connect everything with lines, so set mode='markers' to get markers
# instead
df.iplot(kind='scatter', x='A', y='B', mode='markers')

# bar plot

df2.iplot(kind='bar', x='Category', y='Values')

df.sum().iplot(kind='bar')

df.iplot(kind='box')

# 3d surface plot

df3 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[5,4,3,2,1]})
df3.iplot(kind='surface')


# histogram
df.iplot(kind='hist')

# Spread

df[['A', 'B']].iplot(kind='spread')
df.iplot(kind='bubble', x='A', y='B', size='C')


# scatter matrix

df.scatter_matrix()
