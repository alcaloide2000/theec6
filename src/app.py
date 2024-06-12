from dash import html, dcc
from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "theec practice"

# Function to get data
def get_pandas_data(dfordenada: str) -> pd.DataFrame:
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath('../src/assets').resolve()
    return pd.read_excel(DATA_PATH.joinpath(dfordenada), sheet_name=None)

# GET THE DATA FROM EXCEL
dithe = get_pandas_data("the.xlsx")

# Data for the translation warm-up card
dfthe = dithe['warm']
lcol = dfthe['structure'].unique()
loptions = [{'label': str(option), 'value': option} for option in lcol]

# Card for the warm-up
card_warm = dbc.Card(
    [
        html.H6(
            [html.I(className="fas fa-running fa-3x", style={'color': 'grey'}), ' ',
             'TRANSLATION WARM-UP    .', html.I(className="fas fa-running fa-3x", style={'color': 'grey'})],
            className="class-subtitle"
        ),
        dbc.CardBody(
            [
                html.H4('CHOOSE A STRUCTURE', className="card-title"),
                dcc.Dropdown(loptions, value='all', id='mydrop'),
                html.Div(id='container-button-timestamp0'),
                html.P('click button', className="card-text mt-2"),
                dbc.Button('SPANISH', id='btn-nclicks-1', n_clicks=0, color="info", className="me-1"),
                html.Div(id='container-button-timestamp'),
                dbc.Button('ENGLISH', id='btn-nclicks-2', n_clicks=0, color="primary", className="me-1"),
                html.Div(id='container-button-timestamp2'),
            ],
        )
    ],
    color="danger",
    outline=True,
    style={"width": "100%", "margin": "auto", "padding": "10px"}
)

# Data for the reported speech
dfreport = dithe['reportedsp']
lcolrep = dfreport['story'].unique()
loptionsrep = [{'label': str(option), 'value': option} for option in lcolrep]

# Card for the reported
card_rep = dbc.Card(
    [
        html.H6(
            [html.I(className="fas fa-comments fa-3x", style={'color': 'grey'}), ' ',
             'REPORTED SPEECH     .', html.I(className="fas fa-comments fa-3x", style={'color': 'grey'})],
            className="class-subtitle"
        ),
        dbc.CardBody(
            [
                html.H4('CHOOSE A STORY', className="class-subtitle"),
                dcc.Dropdown(loptionsrep, value='karl and Ana', id='mydroprep'),
                html.Div(id='container-button-timestamp0rep'),
                html.P('click button', className="card-text mt-2"),
                dbc.Button('DIRECT', id='btn-nclicksrep-1', n_clicks=0, color="info", className="me-1"),
                html.Div(id='container-button-timestamprep'),
                dbc.Button('REPORTED', id='btn-nclicksrep-2', n_clicks=0, color="primary", className="me-1"),
                html.Div(id='container-button-timestamp2rep'),
            ],
        )
    ],
    color="danger",
    outline=True,
    style={"width": "100%", "margin": "auto", "padding": "10px"}
)

# Data for the pictures
dfpic = dithe['pictures']

# Card for the pictures
card_pic = dbc.Card(
    [
        html.H6(
            [html.I(className="fas fa-camera fa-3x", style={'color': 'grey'}), ' ',
             'DESCRIBE THE PICTURES', html.I(className="fas fa-camera fa-3x", style={'color': 'grey'})],
            className="class-subtitle"
        ),
        dbc.CardBody(
            [
                html.H4('CHOOSE A PICTURE', className="card-title"),
                html.P('click button', className="card-text mt-2"),
                dbc.Button('PICTURE', id='btn-nclickspic-1', n_clicks=0, color="info", className="me-1"),
                html.Div(id='container-button-timestamppic'),
                dbc.Button('DESCRIPTION', id='btn-nclickspic-2', n_clicks=0, color="primary", className="me-1"),
                html.Div(id='container-button-timestamp2pic'),
            ],
        )
    ],
    color="danger",
    outline=True,
    style={"width": "100%", "margin": "auto", "padding": "10px"}
)

# Data for the interrogative challenge
dfinter = dithe['question']
lcolinter = dfinter['word'].unique()
loptionsinter = [{'label': str(option), 'value': option} for option in lcolinter]

# Card for interrogative
card_inter = dbc.Card(
    [
        html.H6(
            [html.I(className="fas fa-question fa-3x", style={'color': 'grey'}), ' ',
             'INTERROGATIVE CHALLENGE    .', html.I(className="fas fa-question fa-3x", style={'color': 'grey'})],
            className="class-subtitle"
        ),
        dbc.CardBody(
            [
                html.H4('CHOOSE A QUESTION WORD', className="card-title"),
                dcc.Dropdown(loptionsinter, value='all', id='mydropinter'),
                html.Div(id='container-button-timestamp0inter'),
                html.P('click button', className="card-text mt-2"),
                dbc.Button('ANSWER', id='btn-nclicksinter-1', n_clicks=0, color="info", className="me-1"),
                html.Div(id='container-button-timestampinter'),
                dbc.Button('QUESTION', id='btn-nclicksinter-2', n_clicks=0, color="primary", className="me-1"),
                html.Div(id='container-button-timestamp2inter'),
            ],
        )
    ],
    color="danger",
    outline=True,
    style={"width": "100%", "margin": "auto", "padding": "10px"}
)

app.layout = dbc.Container([
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Translation Warm-Up', value='tab-warm', children=[
            dbc.Row([
                dbc.Col(card_warm, width={'size': 12})
            ], justify='center', align='center')
        ], selected_style={'backgroundColor': '#d9534f', 'color': 'white'}, style={'backgroundColor': '#f5f5f5', 'color': 'black'}),
        dcc.Tab(label='Reported Speech', value='tab-rep', children=[
            dbc.Row([
                dbc.Col(card_rep, width={'size': 12})
            ], justify='center', align='center')
        ], selected_style={'backgroundColor': '#d9534f', 'color': 'white'}, style={'backgroundColor': '#f5f5f5', 'color': 'black'}),
        dcc.Tab(label='Interrogative Challenge', value='tab-inter', children=[
            dbc.Row([
                dbc.Col(card_inter, width={'size': 12})
            ], justify='center', align='center')
        ], selected_style={'backgroundColor': '#d9534f', 'color': 'white'}, style={'backgroundColor': '#f5f5f5', 'color': 'black'}),
        dcc.Tab(label='Describe the Pictures', value='tab-pic', children=[
            dbc.Row([
                dbc.Col(card_pic, width={'size': 12})
            ], justify='center', align='center')
        ], selected_style={'backgroundColor': '#d9534f', 'color': 'white'}, style={'backgroundColor': '#f5f5f5', 'color': 'black'}),
    ]),
    dcc.Store(id="didfthe-stored", data=[]),
    dcc.Store(id="diordenadatoday-stored", data=[]),
    dcc.Store(id="didfreport-stored", data=[]),
    dcc.Store(id="diordenadarep-stored", data=[]),
    dcc.Store(id="diordenadapic-stored", data=[]),
    dcc.Store(id="diordenainter-stored", data=[]),
])

if __name__ == '__main__':
    app.run_server(debug=True)