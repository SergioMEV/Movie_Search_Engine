# IMDB Dashboard with Dash

## Libraries
import dash
import pickle
import dash.dash_table as dt
from dash.dependencies import Output, Input
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd

## Importing Data
with open('data/movies.pkl', 'rb') as f:
    movies = pickle.load(f)

movies = movies[0:100000]

## App

app = dash.Dash(external_stylesheets = [dbc.themes.CERULEAN])   # Initializing

### App Layout

## Header navbar
navbar = dbc.Navbar(
    dbc.Container(
        children = 
            [
                dbc.NavbarBrand(html.H1(html.Em("Movie Dashboard"))),
                dbc.Row(
                    [
                        dbc.Col([html.H4("Sergio Martelo")], width = 'auto', style = {'textAlign': 'left'}, align = 'start'),
                    ],
                    justify = "start",       
                )    
            ],
        class_name= 'nav'
    ),
    color = '#276678',
    dark = True,
    light = False,
    class_name = 'nav'
)

## Sidebar

sidebar = dbc.Card(
    [
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.H3("Search", style = {'marginBottom': '2%'}),
                        dbc.Input(id = "name", placeholder = 'Search Titles', type = "text", class_name= 'search'),
                        dbc.Accordion(
                            [
                                dbc.AccordionItem(
                                    [
                                        html.H6('Genre'),
                                        dbc.Checklist(
                                            id = "genre",
                                            options = [
                                                        {'label': 'Animation', 'value': 'Animation'}, 
                                                        {'label': 'Drama', 'value': 'Drama'}, {'label': 'Horror', 'value': 'Horror'}, 
                                                        {'label': 'Adventure', 'value': 'Adventure'}, {'label': 'Mystery', 'value': 'Mystery'}, 
                                                        {'label': 'Western', 'value': 'Western'}, {'label': 'Sci-Fi', 'value': 'Sci-Fi'}, {'label': 'Action', 'value': 'Action'}, 
                                                        {'label': 'Music', 'value': 'Music'}, {'label': 'Comedy', 'value': 'Comedy'}, {'label': 'Fantasy', 'value': 'Fantasy'}, 
                                                        {'label': 'History', 'value': 'History'}, {'label': 'War', 'value': 'War'}, {'label': 'Biography', 'value': 'Biography'}, 
                                                        {'label': 'Crime', 'value': 'Crime'}, {'label': 'Thriller', 'value': 'Thriller'}, {'label': 'Family', 'value': 'Family'},
                                                         {'label': 'Sport', 'value': 'Sport'}, {'label': 'Musical', 'value': 'Musical'}, {'label': 'Romance', 'value': 'Romance'}
                                                      ],
                                            value=1,
                                            inline=True,
                                        ),
                                        html.H6('Runtime'),
                                        dcc.RangeSlider(
                                            id = "runtimerange",
                                            count = 1,
                                            min = 1,
                                            max = 250,
                                            step = 1,
                                            value = [1,250],
                                            marks = {i: "{}".format(i) for i in range(0,250,50)},
                                            tooltip = {'placement': 'bottom'},
                                            allowCross = False
                                        ),
                                        html.H6('Year'),
                                        dcc.RangeSlider(
                                            id = "year",
                                            count = 1,
                                            min = 1900,
                                            max = 2030,
                                            step = 1,
                                            value = [1900,2030],
                                            marks = {i: "{}".format(i) for i in range(1900,2030,20)},
                                            tooltip = {'placement': 'bottom'},
                                            allowCross = False
                                        ),
                                        html.H6('IMDB Rating'),
                                        dcc.RangeSlider(
                                            id = 'IMDBratingrange',
                                            count = 1,
                                            min = 1,
                                            max = 10,
                                            step = 1,
                                            value = [1,10],
                                            marks = {i: "{}".format(i) for i in range(0,10)},
                                            tooltip = {'placement': 'bottom'},
                                            allowCross = False
                                        ),
                                        html.H6('PG Rating'),
                                        dbc.RadioItems(
                                            id = 'pgrating',
                                            options = [{'label': 'TV-14', 'value': 'TV-14'}, {'label': 'TV-G', 'value': 'TV-G'}, 
                                            {'label': 'Approved', 'value': 'Approved'}, {'label': 'G', 'value': 'G'}, 
                                            {'label': 'Passed', 'value': 'Passed'}, {'label': 'R', 'value': 'R'}, 
                                            {'label': 'Not Rated', 'value': 'Not Rated'}, {'label': 'PG-13', 'value': 'PG-13'},
                                            {'label': 'TV-MA', 'value': 'TV-MA'}, {'label': 'TV-PG', 'value': 'TV-PG'},
                                            {'label': 'Banned', 'value': 'Banned'}, {'label': 'PG', 'value': 'PG'}, 
                                            {'label': '22', 'value': '22'}],
                                            inline = True,
                                        )
                                    ],
                                    title = 'Options' ,
                                    class_name= "accordionItem"
                                )
                            ],
                            class_name= 'search'
                        )
                    ],
                    label = "Search",
                    label_style= {'color': '#D3E0EA'},
                    active_label_style= {'color': 'black'}
                ),
                dbc.Tab(
                    [
                        html.H3("Recommendations"),
                        html.P("Lorem Ipsum Dolor")
                    ],
                    label = "Recommendations",
                    label_style= {'color': '#D3E0EA'},
                    active_label_style= {'color': 'black'}
                ),
                dbc.Tab(
                    [
                        html.H3("About"),
                        html.P("Lorem Ipsum Dolor")
                    ],
                    label = "About",
                    label_style= {'color': '#D3E0EA'},
                    active_label_style= {'color': 'black'}
                ),
            ],
        )
    ],
    inverse = False,
    color = '#1687A7'
    )


## Main card

main = dbc.Card(
    [
        dbc.CardBody(
            [
                html.Div(id = 'my-output', style= {'marginBottom': '10%', 'marginTop': '1%'}),
            ],
        )
    ],
    inverse = False,
    color = '#1687A7',
    class_name= 'table'
)

## Layout

app.layout = html.Div(
    # Children 
    children = 
    [
        ## Header
        navbar,
        ## Content
        dbc.Row(
            [
                ### Main 
                dbc.Col(
                    [
                        html.Div(
                            [
                                main
                            ]
                        )
                    ],
                    width = {'size': 5, 'offset': 2}
                ),
                ### Sidebar
                dbc.Col(
                    [
                        html.Div(
                            [
                                sidebar
                            ]
                        ),
                    ],
                    width = {'size': 3, 'offset': 0}
                )
            ],
            style = 
                {
                    'margin-top': '10px',
                }
        )
    ]
    )

## Output functions

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='name', component_property='value'),
    Input(component_id='genre', component_property='value'),
    Input(component_id='runtimerange', component_property='value'),
    Input(component_id='IMDBratingrange', component_property='value'),
    Input(component_id='pgrating', component_property='value'),
    Input(component_id='year', component_property='value'),
)
def update_output_div(name, genre, runtimerange, IMDBratingrange, pgrating, year):
    
    new_df = movies

    ### filter for runtime
    new_df = new_df.loc[(new_df.runtime >= runtimerange[0]) & (new_df.runtime <= runtimerange[1]) | (new_df.runtime is None)]

    ### filter for year
    new_df = new_df.loc[(new_df.year >= year[0]) & (new_df.year <= year[1]) | (new_df.year is None)]

    ### filter for IMDB rating
    
    new_df = new_df.loc[((new_df.IMDB_rating >= IMDBratingrange[0]) & (new_df.IMDB_rating <= IMDBratingrange[1])) | (new_df.IMDB_rating is None)]
    

    ### filter for pgrating
    if type(pgrating) == str and len(pgrating) > 0:
        new_df = new_df.loc[new_df.rating == pgrating]

    ### filter for genre

    if type(genre) == list and len(genre) > 0:
        temp = pd.DataFrame()
        for gen in genre:
            temp = pd.concat([temp, new_df[new_df[gen] == 1]])

        new_df = temp.sort_values('movie')

   

    ### search by input
    if type(name) == str:
        new_df = new_df[new_df['movie'].str.lower().str.contains(name.lower())]

    ## Taking out unnecesary columns

    if len(new_df) == 0:
        new_df = pd.DataFrame(
            {
                'movie': None,
                'year': None,
                'rating': None,
                'runtime': None,
                'IMDB_rating': None,
                'description': None
            },
            index = [0]
        )
    else:
        new_df = new_df[['movie','year', 'rating','runtime','IMDB_rating','description']]

    return html.Div(
            [
                dt.DataTable(
                    data= new_df.to_dict('records'),
                    columns= [{"id": 'movie', "name": 'Movie'}, {"id": 'year', "name": 'Year'}, 
                    {"id": 'rating', "name": 'PG Rating'}, {"id": 'runtime', "name": 'Runtime'}, {"id": 'IMDB_rating', "name": 'IMDB'},
                    {"id": 'description', "name": 'Description'}],
                    style_data= {
                        'whiteSpace': 'normal',
                        'height': 'auto',
                    },
                    style_cell = {
                        'textAlign': 'left',
                        'height': 'auto',
                        'fontFamily': "'Times New Roman'",
                        'minWidth': '60px', 'width': 'auto', 'maxWidth': '180px',
                        'whiteSpace': 'normal'
                    },
                    style_cell_conditional=[
                       {'if': {'column_id': 'runtime'},
                        'width': '90px'},
                    ],
                    style_header_conditional =[
                        {'if': {'column_id': 'rating'},
                         'textAlign': 'left'},
                    ],
                    style_header={
                        'fontWeight': 'bold',
                        'textAlign':'center',
                        'backgroundColor': '#276678',
                        'color':  '#D3E0EA',
                        'fontFamily':"'Courier New'",
                        'padding': '5px'
                    },
                    style_table= {
                        'overflow': 'auto',
                        'height': '1000px'
                    },
                    fixed_rows= {
                        'headers': True
                    },
                    sort_action= 'native'
                )
            ]
        )



def is_genre(row, gen):
    return row.append(pd.Series([not row['genres'].isdisjoint(gen)], ['is_genre']))


def search_input(df, str):

    new_df = pd.DataFrame(columns= ['','movie','year','rating','runtime','genres','IMDB_rating','actors','description','image'])

    if (str is not None) and (len(str) != 0):
        ## filter title
        for ind, x in enumerate(df.movie):
            if str.casefold() in x.casefold():
                new_df = new_df.append(df.iloc[ind])

        ## filter directors and actors
        #for ind, x in enumerate(df.actors):   
        #    if str in ''.join(list(x)).casefold():
        #        new_df = new_df.append(df.iloc[ind])
        
        print("ding")
        return new_df
    else:
        return df




if __name__ == '__main__': 
    app.run_server(debug = True)