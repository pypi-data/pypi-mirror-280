# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2021
Copyright (C) 2021+, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
'''
import base64
import datetime
import io

import dash
from dash import dash_table
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import dash_cytoscape as cyto
import dash_pager

import pandas as pd
import networkx as nx

from importlib import import_module

from matmodel.base import Movelet

from matview.web.view.movelet import movelet_component

# ------------------------------------------------------------
# attributes = ['None']
# sel_attributes = []
# ------------------------------------------------------------
def render_graph_filter(movelets=[], model='', from_value=0, to_value=100, attributes=[], sel_attribute=''):
    return html.Div([
            html.Div([
                html.Div([
                    html.Strong('Attributes: '),
                    dcc.Dropdown(
                        id='input-attr-mov-graph',
                        options=list(map(lambda i: {'label': attributes[i].text, 'value': attributes[i].text}, range(len(attributes)))),
                        value=sel_attribute,
                        style = {'width':'100%'},
                    ),
                #], style={'width': '75% !important', 'flex': 1}),
                ], className='col'),
                html.Div([
                    html.Strong('Graph Format: '),
                    dcc.Dropdown(
                        id='input-format-mov-graph',
                        options=[
                            {'label': 'Sankey Model',    'value': 'sankey'},
                            {'label': 'Markov Model',    'value': 'markov'},
                            {'label': 'Class Heat Map',  'value': 'heatmap'},
                            {'label': 'Movelets',        'value': 'movelets'},
#                            {'label': 'Tree Model',  'value': 'qstree'},
#                            {'label': 'Quality Tree', 'value': 'qtree'},
                        ],
                        value=model,
                        style = {'width':'100%'},
                    ),
                ], style={'marginLeft': '1rem'}, className='col col-lg-3'),
            ], style={'display': 'flex', 'flexDirection': 'row'}),
            html.Div([
                html.Strong('Range of Movelets ('+str(len(movelets))+'): '),
                dash_pager.Pager(
                    id='input-range-mov-graph',
                    value=[from_value, to_value],
                    minValue=0,
                    maxValue=len(movelets),
                    style={'marginLeft': '1rem'},
                ),
            ], style={'display': 'flex', 'flexDirection': 'row', 'marginTop': '1rem'}),
            html.Hr(),
        ], style={'width': '100%'})

def render_graph(movelets=[], model='', from_value=0, to_value=100, sel_attribute=None):
    
    if sel_attribute == '':
        sel_attribute = None

    to_value += 1
    ls_movs = movelets[from_value : 
            (to_value if to_value <= len(movelets) else len(movelets))]
    
    graph_module ='matview.view.mgraph.'
    
    if len(ls_movs) <= 0:
        fig = html.H6('No movelets uploaded ...')
    elif model == 'markov':
        render = getattr(import_module(graph_module+model), 'render')
        G = render(ls_movs, sel_attribute)
        
        fig = cyto.Cytoscape(
            id='graph-'+model,
            layout={'name': 'circle'},
            style={'width': '100%', 'height': '800px'}, #, 'height': '400px'
            elements=G,
            stylesheet=[
                {
                    'selector': 'node',
                    'style': {
                        'background-color': 'data(color)',
                        'line-color': 'data(color)',
                        'label': 'data(label)',
                    }
                },
                {
                    'selector': 'edge',
                    'style': {
                        'curve-style': 'bezier',
                        'background-color': 'data(color)',
                        'line-color': 'data(color)',
                        'target-arrow-color': 'data(color)',
                        'target-arrow-shape': 'triangle',
                        'label': 'data(weight)',
                    }
                }
            ]
        )
    elif model == 'sankey':
        render = getattr(import_module(graph_module+model), 'render')
        G = render(ls_movs, sel_attribute)
        
        fig = dcc.Graph(
            id='graph-'+model,
            style = {'width':'100%'},
            figure=G
        )
    elif model in ['heatmap']:
        if len(ls_movs) > 0:
            render = getattr(import_module(graph_module+model), 'render')
            
            G = render(ls_movs, sel_attribute)
#            print('NUM DEU')
            
#            fig = dcc.Graph(figure=G)
            
            fig = render_img(G)
        else:
            fig = html.Span('No movelets to render.')
            
        fig = html.Div([fig]) 
    elif model == 'movelets':
        
#        maxn = max(map(lambda m: m.size, ls_movs))
        
        fig = html.Div([
#                html.Ul([html.Li([
#                    dcc.RangeSlider(
#                        id='range-mov-points',
#                        min=0,
#                        max=maxn,
#                        value=[0, maxn],
#    #                    tooltip={"placement": "bottom", "always_visible": True}
#                    ),
#                ])]),
                html.Ul(list(map(lambda m:
                    html.Li(html.A(id='tree-link', children=[movelet_component(m)])),
                ls_movs)))
        ], className='movelet')
    elif model == 'tree':
        fig = html.Div(render_tree(ls_movs.copy()))
    elif model == 'qtree':
        fig = html.Div(render_quality_tree(ls_movs))       
    else:
        fig = html.H6('Select a graph format ...')
    
    return [
#        render_graph_filter(movelets, model, from_value, to_value, attributes, sel_attribute),
        html.Div(style = {'width':'100%'}, children = [fig])
    ]

## ------------------------------------------------------------------------------------------------
def render_img(G):
    buf = io.BytesIO() # in-memory files
    G.savefig(buf, format="png") # save to the above file object

    data = base64.b64encode(buf.getbuffer()).decode("utf8") # encode to html elements
    G = "data:image/png;base64,{}".format(data)

    fig = html.Img(
        id='graph-movelets-heatmap',
        style = {'width':'100%'},
        src=G
    )
    return fig
## ------------------------------------------------------------------------------------------------