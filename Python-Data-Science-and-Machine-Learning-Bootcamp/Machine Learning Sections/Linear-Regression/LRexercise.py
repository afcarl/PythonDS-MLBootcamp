from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#try to help company decide whether to focus on mobile app or website

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Linear-Regression/'
customers = pd.read_csv(path + 'Ecommerce Customers')

customers.head()
customers.info()
customers.describe()

### Use seaborn to create a jointplot to compare the Time on Website and
# Yearly Amount Spent columns. Does the correlation make sense? ###

sns.jointplot(customers['Time on Website'], customers['Yearly Amount Spent'])
# There isn't a strong correlation between the two. This sort of makes sense.
# If the website is easy to use, the customer can get in, make a purchase, and get out clean.
# However, it does makes sense that the more time a customer spends on a site, odds are
# They are spending more money.

### Do the same but with the Time on App column instead ###
sns.jointplot(customers['Time on App'], customers['Yearly Amount Spent'])
# Here we see a much stronger correlation. The longer a customer spends on the App
# The more money they spend.

### Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership ###

sns.jointplot(customers['Time on App'], customers['Length of Membership'], kind='hex')
### Let's explore these types of relationships across the entire data set. Use pairplot ###

sns.pairplot(customers)

### Based off this plot what looks to be the most correlated feature with Yearly Amount Spent? ###
# Length of Membership


### Create a linear model plot using seaborn's lmplot comparing Yearly Amount Spent vs Length of Membership ###
sns.lmplot(y='Yearly Amount Spent', x='Length of Membership', data=customers)


### Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column.###

customers.columns
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']]
y = customers['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

### Print out the Coefficients ###
print(lm.coef_)
print(lm.intercept_)


### Predicting Test Data ###
#Now that we have fit our model, let's evaluate its performance by predicting off the test values!

### Use lm.predict() to predict off the X_test set of the data ###
predictions = lm.predict(X_test)

### Create a scatterplot of the real test values vs. the predicted values ###
plt.scatter(y_test, predictions)
plt.xlabel('y_test(Actual)')
plt.ylabel('predicted values')


print('MAE ', metrics.mean_absolute_error(y_test, predictions))
print('MSE', metrics.mean_squared_error(y_test, predictions))
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# calculate the explained variance
metrics.explained_variance_score(y_test, predictions)


sns.distplot((y_test-predictions), bins=50)

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients
