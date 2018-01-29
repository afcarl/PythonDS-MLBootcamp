import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2
fig = plt.figure()


ax = fig.add_axes([0,0,1,1])


# color arg takes common color names, or typical #colorcodes, alpha is trasparency, marker
# marks where the exact points in the set are
ax.plot(x,y, color='#000000', linewidth=1, alpha=1, linestyle='-', marker='o', markersize=10,
        markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='blue')

#this only shows the plot from x=[0,1]
ax.set_xlim([0,1])
ax.set_ylim([0,2])

# Special plot types like scatter() hist() boxplot() can be used with matplotlib
# But we will be using Seaborn for these types of graphs
