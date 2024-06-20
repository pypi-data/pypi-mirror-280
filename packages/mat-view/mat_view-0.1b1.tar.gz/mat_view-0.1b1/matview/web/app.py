# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2021
Copyright (C) 2021+, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
'''
import sys, os 

import pandas as pd
#sys.path.insert(0, os.path.abspath(os.path.join('.')))

import base64
import datetime
import io

import dash
from dash import dash_table
import dash_pager
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

#from automatize.assets.routes.page_analysis import render_page_analysis
#from automatize.assets.routes.page_datasets import render_page_datasets
#from automatize.assets.routes.page_experiments import render_page_experiments
#from automatize.assets.routes.page_results import render_page_results

from matview.web.app_base import *
from matview.web.config import *
# ------------------------------------------------------------

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return render_page_home()
    else:
        from importlib import import_module
        module = import_module('matview.web.'+pathname[1:].split('/')[0]+'.main')
        return module.render(pathname)
#    elif pathname == '/analysis':
#        return render_page_analysis()
#    elif pathname == '/methods':
#        return render_markdown_file(PAGES_ROUTE+'assets/pages/methods.md', div=True)
#    elif '/datasets' in pathname:
#        return render_page_datasets(pathname)
#    elif pathname == '/experiments':
#        return render_page_experiments(pathname)
#    elif pathname == '/results':
#        return render_page_results(pathname) #render_markdown_file('./assets/experiments.md')
#    elif pathname == '/publications':
#        return render_markdown_file(PAGES_ROUTE+'publications.md', div=True)
#    elif pathname == '/tutorial':
#        return html.Div(id='content-home', children=[html.Iframe(
#            src="assets/examples/Automatize_Sample_Code.html", width="100%", height="100vh",
#            style={"height": "100vh", "width": "100%"},
#        )])
#    else:
#        file = ASSETS_ROUTE + pathname+'.md'
#        #print(os.path.abspath(file))
#        if os.path.exists(file):
#            return render_markdown_file(file, div=True)
#        else:
#            return underDev(pathname)
#    # You could also return a 404 "URL not found" page here
    
y = datetime.datetime.now().date().year
    
light_logo = True
app.layout = html.Div(id = 'parent', children = [
        html.Nav(className='navbar navbar-expand-lg navbar-dark bg-primary', 
            style={'paddingLeft': '1rem', 'paddingRight': '1rem'},
            id='app-page-header',
            children=[
                # represents the URL bar, doesn't render anything
                dcc.Location(id='url', refresh=False),
                html.A(className='navbar-brand',
                    children=[
                        html.Img(src='../assets/img/favicon.ico', width="30", height="30"),
                        page_title,
                    ],
                    href="/",
                ),
                html.Div(style={'flex': 'auto'}),#, children=[
                html.Ul(className='navbar-nav', children=[
                    html.Li(className='nav-item', children=[
                     html.A(className='nav-link',
                         children=['Home'],
                         href="/",
                     ),
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link',
                            children=['About'],
                            href="https://github.com/mat-analysis",
                        ),
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link nav-link-btn',
                            id='gh-link',
                            children=['GitHub'],
                            href="https://github.com/mat-analysis/mat-tools",
                        ),
                    ]),
                ]),
            ],
        ),
    
        html.Div(id='page-content'),
    
        html.Hr(),
        html.Span('© '+str(y)+' version '+VERSION+', by ', style={'marginLeft': '1rem'}),
        html.A(
            children=['Tarlis'],
            href="https://tarlis.com.br",
        ),
        html.Span(' in '),
        html.A(
            children=['mat-analysis'],
            href='https://github.com/mat-analysis',
        ),
        html.Span('.'),
        
        html.Div('', id='load-screen', className='load-screen', 
                 style={'visibility': 'hidden'}
        ),
        html.Div([ # Workaround for importing components TODO**
            dash_pager.Pager(maxValue=0),
        ], style={'display': 'none'})
    ]
)

def render_page_home():
#     return render_markdown_file(README)
    return html.Div(id='content-home', children=[ 
#        render_markdown_file(README, div=True),
        html.Div(className='row card-columns', style={'marginLeft': '1rem', 'marginRight': '1rem'}, 
                 children=[render_card(*m) for m in MODULES]),
#     ], style={'margin': '20px'})
    ])

def render_card(title, desc, url):
    return dbc.Card([
    #            dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                dbc.CardBody(
                    [
                        html.H4(title, className="card-title"),
                        html.P(
                            desc,
                            className="card-text",
                        ),
                        dbc.Button("Go", color="primary", href=url, className="stretched-link"),
                    ]
                ),
            ],
            style={"width": "18rem", 'marginTop': '1rem'},
        )

if __name__ == '__main__':
#     sess.init_app(app)
    app.run_server(host=HOST, port=PORT, debug=DEBUG)