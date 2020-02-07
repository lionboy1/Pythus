import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div( children = [
    html.H1('Welcome to your dashboard.'),
    dcc.Graph( id='Demo dashboard',
            figure={'data': [
                { 'x': [1,2,3], 'type': 'bar', 'name': 'first chart'},
                { 'y': [4,5,6], 'type': 'bar', 'name': 'second chart' }
            ],
                   'layout': { 'Title': 'Bar plots'}})
            
])


if __name__ == '__main__':
    #app.run() - run on hosted account
    #app.run_server() - run on local server
