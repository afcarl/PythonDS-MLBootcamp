#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Matrix Plots

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()

# Heatmaps
# in order to display a heatmap, our data must be in matrix form, meaning the
# rows and columns must both be variables. We use this typically through
# pivot tables and/or corr

# corr first
tc = tips.corr()
# heatmap() takes in your dataset, 'annot=True/False' which will display the actual
# values of the data on the heatmap, and cmap='' which takes in a color scheme
sns.heatmap(tc, annot=True, cmap='coolwarm')

# Pivot Tables
fp = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fp, cmap='magma', linecolor='white', linewidth=1)


# Cluster Maps will try to produce a heatmap with the similar colors next to each other
# standard_scale= will normalize the map, sometimes making it easier to read
sns.clustermap(fp, cmap='coolwarm', standard_scale=1)
