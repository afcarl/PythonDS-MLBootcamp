#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# categorical plots

tips = sns.load_dataset('tips')
tips.head()

# Bar Plot will show you the mean by default, but we can change the 'estimator object'
# to np.std to compare the standard deviations instead of the means

sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

# countplot() takes in an x value and data, then counts the number of occurences
# of the x, and plots it on the y axis

sns.countplot(x='sex', data=tips)

# Box plots will show you the 4 quartiles, and outliers
# we can add hue='' to break up the x values into further columns

sns.boxplot(x='day',y='total_bill', data=tips)

# Violin Plot give you the same information as a boxplot, but the violinplot will
# show more information. Also takes the hue args. This also takes 'split', which
# combines your hue into 1 column


### SPLIT HAS BEEN REPLACED BY DODGE()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# stripplot() draws a scatterplot where one variable is categorical, although
# it is hard to get real info from this because the points are too squished.
# to combat this, we add an args 'jitter'

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', dodge=True)


# swarmplot is essentially a combination of a violinplot and a scatterplot
# Though, they don't always scale well for large datasets

sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

# Factor plot is the most common way of calling all of these plots, simply
# specify what type of plot you want in the kind='' args
sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')
