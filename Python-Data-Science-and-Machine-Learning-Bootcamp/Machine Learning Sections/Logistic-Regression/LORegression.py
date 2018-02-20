#!/usr/bin/python3
import numpy as np
import pandas as pd
import seaborn as sns
import cufflinks as cf
cf.go_offline()
import matplotlib.pyplot as plt
%matplotlib inline

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Logistic-Regression/'
train = pd.read_csv(path+ 'titanic_train.csv')

train.head()
# SibSp indicates the number of siblings or spouses aboard.
# Parch indicates the number of children or parents on board

# Use seaborn to show where we are missing data

sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='plasma')
# yellow dash show "true" points (null values, missing information)
# We are missing a ton of age and cabin data. Luckily age is small enough that
# we can probably supplement it.

sns.set_style('whitegrid')

sns.countplot(x='Survived', data=train, hue='Sex')
# 0 indicates they did not survive
# If someone survived, they are much more likely to be female.

sns.countplot(x='Survived', data=train, hue='Pclass')
# Those in the third class faired the worst. 2nd class was about 50/50,
# 1st class was the only class where the survival rate was about 50%

sns.distplot(train['Age'].dropna(), kde=False, bins=30)
# There was a spike in infant deaths, but a large number of people who died
# were 20-30


train.info()
sns.countplot(x='SibSp', data=train)
# more than 600 people had no siblings or spouse on board, the next most common
# is someone with 1 sibling or spouse

sns.distplot(train['Fare'], kde=False, bins=50)
# this makes sense that the cheaper tickets (the ones in the 3rd class) had the highest
# casualties

# Doing a similar thing in pyplot
train['Fare'].iplot(kind='hist', bins=50)



# Using imputation to fill in the age column
plt.figure(figsize=(10,7))
sns.boxplot(x='Pclass', y='Age', data=train)
# On average, as the class gets nicer, the age of the person goes up.

# Just using simple imputation to fill in the age of the missing passengers

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            # this will calculate the average age of those in the first class
            return train[train['Pclass']==1]['Age'].mean()
        elif Pclass == 2:
            return train[train['Pclass']==3]['Age'].mean()
        else:
            return train[train['Pclass']==1]['Age'].mean()
    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='plasma')
# now we have filled in all of the missing data for our age column
# The cabin column has too much missing info, so we drop it.
train.drop('Cabin', axis=1, inplace=True)

# Now we have no missing values
train.dropna(inplace=True)


# We need to crete a dummy variable for categorical variables
sex = pd.get_dummies(train['Sex'], drop_first=True)
# we use drop_first=True to avoid a mutiple collinearity issue with our ML program.
# we don't need to know if someone is male and if they are female, either info will do.
# So we drop the dead weight.

sex.head()
embark = pd.get_dummies(train['Embarked'], drop_first=True)
embark.head()
train = pd.concat([train, sex, embark], axis=1)
train.head()

# we now drop all of the non-numerical, hard to interpret data
train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
train.drop(['PassengerId'], axis=1, inplace=True)
train.head()

# remember if Q=1 then Q, if S=1 then S, if S=Q=0, then C=1


X = train.drop('Survived', axis=1)
y = train['Survived']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, predictions))

# and here we have trained and predicted values from the train.csv file. We can explore
# by using the entire train.csv as a training set and the test.csv as a test set.
