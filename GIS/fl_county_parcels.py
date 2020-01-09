# refer to https://github.com/plotly/plotly.py/issues/1660 to fix plotly install errors

import pandas as pd
import plotly.figure_factory as ff

df = pd.read_excel('county_parcels.xlsx', converters={'state code': lambda x: str(x), 'county code': lambda x: str(x) })
df['FIPS'] = df['state code'] + df['county code']
df.head(6)

fips = df['FIPS'].tolist()
values = df['parcels'].tolist()
colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

figure = ff.create_choropleth(
    fips=fips, values=values, scope=['FL'],
    binning_endpoints=[10000, 20000, 30000, 50000, 65000, 75000, 95000, 115000, 125000, 
                       145000, 165000, 185000, 200000, 250000, 285000],
    colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    round_legend_values=True,
    legend_title='Land Parcels by County', title='Florida Counties')
fig.layout.template = None
fig.show()

