from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#try to predict housing prices based off of features

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Linear-Regression/'
df = pd.read_csv(path + 'USA_Housing.csv')

df.head()

df.info()

df.describe()

sns.pairplot(df)

sns.distplot(df['Price'])
sns.heatmap(df.corr(), annot=True)



df.columns

# Now need to create train and test sets.
### Grabbing predictors I want to test in X
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]

#Values I want to test on go in y
y = df['Price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=101)

# test_size is the percentage of the data set to include in the test set
# random_state is used to specify a specific randomness (basically use to keep up with the course)

lm = LinearRegression()
lm.fit(X_train, y_train)
# Here we have trained the model to our train set. Now we can call various functions off of it to get
# information. We will pass the coefficients to a dataframe The coefficients are presented in an
# array and are in the same order as the Index of X
print(lm.intercept_)

print(lm.coef_)

pd.DataFrame(data = lm.coef_, index = X.columns, columns=['Coefficients'])

from sklearn.datasets import load_boston
# load_boston is a real-dataset for Bston Houses
boston = load_boston()
boston.keys()
print(boston['DESCR'])


######################################
############### PART TWO #############
######################################


# Predictions

predictions = lm.predict(X_test)
# Predictions now holds the predicted prices of the houses.
# We compare this against our real prices in y_test
predictions

plt.scatter(y_test, predictions)

# the closer to a straight line the better. This is pretty good

sns.distplot((y_test-predictions))
# A normal distribution from a distplot shows you chose a good model

from sklearn import metrics
# Calculating MAE, MSE, RMSE

metrics.mean_absolute_error(y_test, predictions)
metrics.mean_squared_error(y_test, predictions)
np.sqrt(metrics.mean_squared_error(y_test, predictions))
