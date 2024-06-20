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
#import dash_pager
#from matdata.preprocess import readDataset, organizeFrame

#from matview.web.app_base import app, sess, gess
from matview.web.app_base import sess, gess
from matview.web.config import WEB_ROUTE, render_markdown_file, underDev

from matview.web.view.mat import render_mat_filter
from matview.web.view.graph import render_graph_filter

from matview.web.view.callback import *

# ------------------------------------------------------------
def reset():
#     global from_trajs, to_trajs, sel_attributes, sel_traj, ls_tids, ls_trajs, ls_movs
    sess('from_trajs', 0)
    sess('to_trajs', 50)
    sess('sel_attributes', [])
    sess('sel_traj', '')
    # ------------------------------------------------------------
    sess('ls_tids', [])
    sess('ls_trajs', [])
    sess('ls_movs', [])

# ------------------------------------------------------------
def render(pathname):
    reset()
    return dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Upload', value='tab-1', children=[render_content('tab-1')]),
        dcc.Tab(label='MAT View', value='tab-2', children=[render_content('tab-2')]),
        dcc.Tab(label='MAT x Movelets', value='tab-3', children=[render_content('tab-3')]),
        dcc.Tab(label='Graphs', value='tab-4', children=[render_content('tab-4')]),
    ]),

# @app.callback(Output('tabs-content', 'children'),
#               Input('tabs', 'value'))
def render_content(tab):
    
    from_trajs     = gess('from_trajs', 0)
    to_trajs       = gess('to_trajs', 100)
#     sel_attributes = sess('sel_attributes', [])
    sel_traj       = gess('sel_traj', '')    
    
    if tab == 'tab-1':
        return html.Div([
            html.H4('Upload Files'),
            html.Span('Upload dataset files (for MAT) and JSON files of movelets for visualizing the data.'), 
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
    #                 'width': '90%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'marginTop': '1rem',
                    'marginBottom': '1rem',
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ], style = {'margin':'1rem'})
    elif tab == 'tab-2':
        return html.Div(style = {'margin':'1rem'}, children=[
            html.H4('MAT and Movelets Visualization'), 
            html.Div(id='filter-mat', children=[
                render_mat_filter([], from_trajs, to_trajs, [], []),
            ]),
            html.Div(id='output-mats'),
        ])
    elif tab == 'tab-3':
        return html.Div(style = {'margin':'1rem'}, children=[
            html.H4('Movelets Visualization'), 
            html.Div(id='filter-mat-movelet', style = {'display':'inline'}, children = [
                html.Strong('Trajectory ID: '),
                dcc.Input(
                    id='input-traj',
                    placeholder='TID...',
                    type='text',
                    value=str(sel_traj)
                ),
            ]),
            html.Div(id='output-mat-movelet'),
        ])
    elif tab == 'tab-4':
        return html.Div(style = {'margin':'1rem'}, children=[
            html.H4('Graph Visualizations'), 
            html.Div(id='filter-graph', children=[
                render_graph_filter(),
            ]), 
            html.Div(id='output-graph'),
        ])
    else:
        return html.Div([
            dbc.Alert("Content in development.", color="info", style = {'margin':'1rem'})
        ])
