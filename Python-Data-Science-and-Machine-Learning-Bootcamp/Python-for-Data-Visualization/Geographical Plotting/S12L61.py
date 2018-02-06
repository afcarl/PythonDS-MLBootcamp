#!/user/bin/python3

#Choropleth Maps - USA Part 1

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

import pandas as pd
data = dict(type='choropleth',
        locations = ['AZ', 'CA', 'NY'],
        locationmode = 'USA-states',
        colorscale  = 'Greens',
        text = ['text 1', 'text 2', 'text 3'],
        z = [1.0, 2.0, 3.0],
        colorbar = {'title': 'Colorbar Title Here'})
layout = dict(geo={'scope':'usa'})
choromap = go.Figure(data = [data], layout = layout)

# exports as an html file!!!
iplot(choromap)

path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Geographical Plotting/'
df = pd.read_csv(path + '2011_US_AGRI_Exports')

df.head()



data = dict(type = 'choropleth',
        colorscale = 'YIOrRd',
        locations = df['code'],
        locationmode = 'USA-states',
        z = df['total exports'],
        text = df['text'],
        colorbar = {'title': 'Millions USD'},
        marker = dict(line = dict(color = 'rgb(255,255,255)', width=2))) # marker draws a border around each state

layout = dict(title = '2011 US Agriculture Exports by State',
        geo = dict(scope='usa', showlakes = True, lakecolor='rgb(85, 173, 240)'))

choromap2 = go.Figure(data = [data], layout = layout)
iplot(choromap2)
