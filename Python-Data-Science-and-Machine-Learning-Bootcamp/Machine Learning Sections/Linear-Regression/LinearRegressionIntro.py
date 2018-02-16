#!/usr/bin/python3

from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.cross_validation import train_test_split

# You should split your data into a train set and a test set, use train_test_split
# to accomplish this

X, y = np.arange(10).reshape(5,2), range(5)

X
list(y)

# Now we have some boring data to split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train
X_test

y_train
y_test

# Now everything is nice and split up into training and testing datasets

# we now train/fit our model on the training data using model.fit()
# model.score() returns a value [0,1], the closer to 1 the better the fit
