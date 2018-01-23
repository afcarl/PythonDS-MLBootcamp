# GroupBy

import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df

byCompany = df.groupby('Company')
# Panda ignores any non-numeric column when using aggregate functions on dataframes
byCompany.mean()
byCompany.sum()
byCompany.std()

byCompany.sum().loc['FB']

# Same as above but done in one line
df.groupby('Company').sum().loc['FB']

# This tallies all countable things by company
df.groupby('Company').count()

# when calling max() on a string, it will return the string which is closest to the
# end of the alphabet

# likewise, min() returns the string closest to the beginning of the alphabet
df.groupby('Company').max()


# Super useful!!!!!
df.groupby('Company').describe()

df.groupby('Company').describe().transpose()
