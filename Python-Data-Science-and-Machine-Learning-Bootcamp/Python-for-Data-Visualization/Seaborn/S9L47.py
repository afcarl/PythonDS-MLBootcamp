#!/usr/bin/python3
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# 'tips' is just a default dataset that comes with seaborn
tips = sns.load_dataset('tips')
tips.head()

# we can add kde=False to remove the curve, also, we add bins=30 to show 30 bars on the graph
# we can keep increasing bids up to the index size to get a more
# precise view of our data
sns.distplot(tips['total_bill'], kde=False, bins=40)

# JointPlot allows you to combine two distplots. Here we plot the total_bill amount
# on the x-axis and the tip amount on the y-axis. This creates a joinplot with bars
# on the axes and a scatterplot.

# kind=''is scatter by default, but this controls what sort of graph is displayed
# on the plot. We pass in 'hex' to display a hexagraph

sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde', color='blue')

# pairplot will plots all of the columns and rows against each other
# this is a great way to quickly visualize your data.
# hue='' takes in a categorical (True/False, Male/Female, etc.) column and will
# separate and plot these on the pairplot graph. it also takes palette='' which
# allows you to set the colors yourself
sns.pairplot(tips, hue='sex')

# a rugplot draws one small line for each value in the single column. seems to be
# less useful than a histogram (distplot())
sns.rugplot(tips['total_bill'])

# KDE plots = Kernel Density Estimation plots
# create a dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset)

# set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally space points from x_min to x_max
x_axis = np.linspace(x_min, x_max, 100)

# set up the bandwidth
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2

# initialize an empty kernel list
kernel_list =[]

#Plot each basis function
for data_point in dataset:
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    #scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * 0.4
    plt.plot(x_axis, kernel, color = 'grey', alpha=0.5)

plt.ylim(0,1)

# KDE plots are the sum of all of the normal distribution plots
