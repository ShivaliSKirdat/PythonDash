import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# set a variable to use the Flask server
server = flask.Flask(__name__)
# Pass the Flask server into Dash to be called
app = dash.Dash(__name__,  server=server, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Load the CSV file that contains the city data
# 'usecols' specifies only the columns I want to be read in
# 'nrows' reads the first 50 rows into frame
df_csv = pd.read_csv('./data/uscities.csv', usecols=['city', 'state_id', 'population', 'density'], nrows=50)

fig = px.bar(df_csv, x="city", y="population", color="density", barmode="group", labels={'density': 'Density per sq. mile', 'population': 'Population', 'city': 'City'})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(
        children='US City Population and Density (staging)',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.A(
        href='https://simplemaps.com/data/us-cities', 
        children='''
            Data provided by simplemaps.com
        ''',
        style={
            'display': 'flex',
            'justifyContent': 'center',
            'color': colors['text'],
        },
    ),

    html.Div(
        children='''
            An outlook on US City total population and density(per sq. mile)
        ''',
        style={
            'textAlign': 'center',
            'color': colors['text'],
        }),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
