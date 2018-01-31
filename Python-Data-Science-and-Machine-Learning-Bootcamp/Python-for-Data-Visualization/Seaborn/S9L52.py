#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


tips = sns.load_dataset('tips')
tips.head()

'''
sns.set_context('notebook')
sns.countplot(x='sex', data=tips)
'''

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')
