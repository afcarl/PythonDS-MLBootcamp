#!/usr/bin/python3
# First Matplotlib lesson

import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,5,11)
y = x ** 2



#plt.plot(x,y)
# typically use plt.show() to display the plot, but I don't have to because of
# the hydrogen plugin-in

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')

# Multi-plots on the same canvas

#creates a plot that maps x vs y and makes it red
#plt.subplot(1,2,1)
#plt.plot(x,y,'r')

#creates a plot that maps y vs x and makes it blue
#plt.subplot(1,2,2)
#plt.plot(y,x,'b')

# object oriented method

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes.plot(x,y)

axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

#axes1.plot(x,y)
axes1.set_title('Larger Plot')


#axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')


### PART 2 ###

# use nrows and ncols as args for .subplots()
# fig, axes = plt.subplots(nrows=1, ncols=2) will yield two graphs on one row

fig,axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')

# figsize sets size in l x w
fig = plt.figure(figsize=(8,2))
#ax = fig.add_axes([0,0,1,1])
#ax.plot(x,y)

fig, axes = plt.subplots(nrows = 2, ncols=1, figsize=(8,2))

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()



# how to save a figure

fig.savefig('my_picture.png')


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='X Squared')
ax.plot(x,x**3, label='X Cubed')


# There are location codes in the pyplot documentation that move the legend,
# legend(loc=0) should be default, but this sets the "best location" for the
# legend
ax.legend()

























#
