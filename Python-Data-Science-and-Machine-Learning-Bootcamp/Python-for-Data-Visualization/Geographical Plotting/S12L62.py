#!/user/bin/python3

#Choropleth Maps - Global

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import pandas as pd

path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Geographical Plotting/'
df = pd.read_csv(path + '2014_World_GDP')
df.head()

data = dict(type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title': 'GDP in Billions USD'})

layout = dict(title= '2014 Global GDP',
        geo = dict(showframe=False, projection={'type': 'natural earth'}))

choromap3 = go.Figure(data =[data], layout = layout)
iplot(choromap3)
