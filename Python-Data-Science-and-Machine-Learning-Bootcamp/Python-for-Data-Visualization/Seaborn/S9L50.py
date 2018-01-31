#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Grids

iris = sns.load_dataset('iris')
iris.head()
'''
sns.pairplot(iris)
# PairGrid creates the plots you see in pairplot, but empty
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
'''
tips = sns.load_dataset('tips')

g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
