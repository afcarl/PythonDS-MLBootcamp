#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Regression Plots

tips = sns.load_dataset('tips')
tips.head()

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'])

sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')
