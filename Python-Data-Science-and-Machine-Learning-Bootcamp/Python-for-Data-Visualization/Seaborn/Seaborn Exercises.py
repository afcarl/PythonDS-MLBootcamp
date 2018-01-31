#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

sns.jointplot(x='fare', y='age', data=titanic)

sns.distplot(titanic['fare'], kde=False, bins=30)

sns.boxplot(x='class', y='age', data=titanic)
sns.swarmplot(x='class', y='age', data=titanic)

sns.countplot(x='sex', data=titanic)

tc = titanic.corr()
sns.heatmap(tc, cmap='coolwarm')

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')
