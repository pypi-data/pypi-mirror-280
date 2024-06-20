import os

from dash import html
import dash_bootstrap_components as dbc

from matview.web.config import WEB_ROUTE, render_markdown_file, underDev

# ---------------------------------------------------------------------------------
METHODS_TYPES = [
    {'title': 'Classification', 'description': 'Classification methods', 'filename': 'classification.md'},
    {'title': 'Summarization',  'description': 'Summarization methods',  'filename': 'summarization.md'},
    {'title': 'Similarity',     'description': 'Similarity functions',   'filename': 'similarity.md'},
    {'title': 'Clustering',     'description': 'Clustering methods',     'filename': 'clustering.md'},
]

def render(pathname):
    if pathname == '/method':
        return html.Div(className='row', style={'margin': '1rem'}, children=
            [
                html.H1('Methods'),
                html.Hr(),
                dbc.ListGroup(
                    [dbc.ListGroupItem([
                            html.Div(
                                [
                                    html.H5(f['title'], className="mb-1"),
#                                    html.Small("Yay!", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.P(f['description'], className="mb-1"),
                            html.Small(f['filename'], className="text-muted"),
                        ], href="/method/"+ f['filename']
                    ) for f in METHODS_TYPES]
                ),
                html.P(id="counter"),
            ]
        )
    elif pathname[-2:] == 'md':
        return html.Div(style = {'margin':'1rem'}, children=[
#             html.H3('Datasets'), 
            render_markdown_file(WEB_ROUTE+pathname),
        ])
        return render_dataset(pathname)
    else:
        return underDev(pathname)