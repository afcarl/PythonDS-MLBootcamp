# DataFrames
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(data=randn(5,4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
df

# Grabbing values from the 'W' column
df['W']

# A dataframe is just a bunch of series that share an index

# Can also use SQL-like notation like below - this can get confusing with the given methods from pandas,
# so try to use bracket notation
df.W

# Pass in a list to grab multiple series, aka a dataframe

df[['W', 'Z']]

# defining new columns
df['new'] = df['W'] + df['Y']
df

# This will throw an error, as the 'axis' is set to '0', as in it's searching the index or the rows for this
#df.drop('new')

# Note these changes are not saved, calling 'df' will still show the 'new' column
df.drop('new', axis=1)

# in order to save those changes, add the args 'inplace=True'
df.drop('new', axis=1, inplace=True)

df

# drop() can be used to drop rows with 'axis=0'

df.drop('E', axis=0)

# df.shape will give you the shape of the dataframe

df.shape

# Selecting rows, use loc to return a series

df.loc['A']

# iloc will grab a row based off of it's index location

df.iloc[2]

# This grabs the specific value at (B,Y)
df.loc['B', 'Y']


df.loc[['A', 'B'], ['W', 'Y']]


#################################
###       PART 2 - S6L27      ###
#################################

df

booldf = df > 0

df[booldf]
df[df > 0]

df['W'] > 0

df[df['W'] > 0]
df[df['Z'] < 0]

resultdf = df[df['W'] > 0]

# This will return the X column of the dataframe where the rows in column W that have values
# less than 0 have been removed
df[df['W']>0]['X']

# multiple conditions - use & in place of 'and' as well as | in place of 'or'

df[(df['W']>0) | (df['Y']>1)]

df

df.reset_index()

# Neat trick to make a list
newind = 'CA NY WY OR CO'.split()

df['States'] = newind
df

# This will make the States column the new index - must use inplace=True to keep the values
df.set_index('States')

#################################
###       PART 3 - S6L28      ###
#################################


oustide = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(oustide, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# This creates a data frame of random numbers in a 6x2 matrix using the indexes from hier_index as well as the G levels
# with columns named A&B
df = pd.DataFrame(data=randn(6,2), index=hier_index, columns=['A', 'B'])

df

df.loc['G1']

df.index.names = ['Groups', 'Num']

df

# When grabbing variables, remember to use .loc[] when sorting through dataframes,
# Once you get down to a series like on line 126, you can go back to sorting as if
# sorting through a series like in line 128

df.loc['G2'].loc[2]
df.loc['G2'].loc[2]['B']

# XS - Cross-Section

# This will grab a crossection of the dataframe where the index under 'Num' is equal to '1'
df.xs(1, level='Num')
