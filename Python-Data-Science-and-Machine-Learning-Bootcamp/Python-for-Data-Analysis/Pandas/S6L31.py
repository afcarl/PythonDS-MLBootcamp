import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# pd.concat([list, of, dataframes, to, concatenate, on]) Dims along axis must match,
# defaults to axis=0, but you can concat along axis=1. NOTE: NaN will fill in all missing values

# pd.merge(left, right, how='inner', on='key') very similar to SQL
# will merge DataFrames 'left' & 'right' on the 'key' column


# left.join(right) will join columns of the dataframes 'left & 'right' together and will fill in 
# empty data slots with NaN
