import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import __version__
import cufflinks as cf
import seaborn as sns
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
%matplotlib inline

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/'

df = pd.read_csv(path + '911.csv')
df.head()
df.info()

#What are the top 5 zipcodes? (most common?)
df['zip'].value_counts().nlargest(5)

# What are the top 5 twp for 911 calls
df['twp'].value_counts().nlargest(5)

# How many unique title codes are there?
df['title'].nunique()

'''
Creating new features
In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic.
Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
'''

df['title'].apply(lambda x: x.split(':')[0])

df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])

df['Reason'].value_counts()


sns.countplot(df['Reason'])


# convert DateTime column to actual date times

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
stamp1 = df['timeStamp'].iloc[0]
stamp1.month


# create Month, Day, Hour columns

df['Month'] = df['timeStamp'].apply(lambda date: date.month)
df['Day of Week'] = df['timeStamp'].apply(lambda date: date.dayofweek)
df['Hour'] = df['timeStamp'].apply(lambda date: date.hour)

# convert day to days of the week

date_map = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

df['Day of Week'] = df['Day of Week'].map(date_map)

df['Day of Week']

#Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.

sns.countplot(df['Day of Week'], hue=df['Reason'])

# Do the same for Month


month_map = {0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'June', 6: 'July', 7:'Aug', 8:'Sep', 9:'Oct', 10:'Nov', 11:'Dec'}

df['Month'] = df['Month'].map(month_map)

df['Month']
sns.countplot(df['Month'], hue=df['Reason'])

# Need to fill in Missing Months

byMonth = df.groupby('Month').count()
byMonth.head()

byMonth['twp'].plot()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

df['Date']=df['timeStamp'].apply(lambda t: t.date())


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()





df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


sns.clustermap(dayHour,cmap='viridis')

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')

sns.clustermap(dayMonth,cmap='viridis')
