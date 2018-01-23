# Missing Data

import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
df

# dropna - pandas will drop any row with at least 1 missing value with axis=0, same can be done for columns
# axis=1

df.dropna()

# thresh sets the number of nans needed for the row/column to be dropped. thresh=2 will drop any row/column with 2 or more nans
df.dropna(thresh=2, axis=0)

# fillna

df.fillna(value='FILL VALUE')

# this will fill the missing value in A with the mean of the other values
df['A'].fillna(value=df['A'].mean())
