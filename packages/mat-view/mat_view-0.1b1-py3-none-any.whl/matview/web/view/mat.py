# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2021
Copyright (C) 2021+, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
'''
import os 
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..','mat-model-pkg'))) # TEMP

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
import dash_pager

from tqdm.auto import tqdm

from matmodel.base import Trajectory
from matmodel.base import Movelet
from matmodel.util.filters import names2indexes, attributes2names

# ------------------------------------------------------------
def render_mat_filter(ls_trajs, from_trajs, to_trajs, attributes, sel_attributes):
    if len(ls_trajs) > 0:
        import random
        T = random.sample(ls_trajs, 1)[0]
        SIZE = getAttrSize(T, []) # in chars
    
    return html.Div([
        html.Div([
            html.H6('Aspects: '),
            dcc.Dropdown(
                id='input-attr-traj',
                options=list(map(lambda i: {'label': attributes[i].text, 'value': i}, range(len(attributes)))),
                multi=True,
                value=",".join(map(str,sel_attributes))
            ),
        ]),
        html.Div([
            html.Strong('Range of Trajectories ('+str(len(ls_trajs))+'): '),
            dash_pager.Pager(
                id='input-range-mats',
                value=[from_trajs, to_trajs],
                minValue=0,
                maxValue=len(ls_trajs),
                style={'marginLeft': '1rem'},
            ),
        ], style={'display': 'flex', 'flexDirection': 'row', 'marginTop': '1rem'}),
        html.Hr(),
    ], style = {'display':'inline'})    

def render_mat(ls_trajs, range_value, ls_movs, sel_attributes):
    ncor = 7
    ls_components = []
    
    
    if len(ls_trajs) > 0:
        attributes, sel_attributes = getSelection(ls_trajs, sel_attributes)
        
        size = SIZE #getAttrSize(T, sel_attributes) # in chars
                
        
        from_trajs, to_trajs = range_value
        from_trajs = from_trajs if from_trajs < len(ls_trajs) else 0
        to_trajs = to_trajs if to_trajs < len(ls_trajs) else to_trajs if to_trajs >= from_trajs else from_trajs
        
#        ls_components.append(render_mat_filter(ls_trajs, from_trajs, to_trajs, attributes, sel_attributes))

#        ls_trajs = ls_trajs[(from_trajs if from_trajs < len(ls_trajs)-1 else 0) : (to_trajs if to_trajs < len(ls_trajs)-1 else 100)]
        ls_trajs = ls_trajs[from_trajs : to_trajs]

        def renderT(k):
            nonlocal ls_trajs, ls_components
    #         points = T.points_trans()
            T = ls_trajs[k]
            ls_components.append(html.Div(className='traj-color'+str((k % ncor) + 1)+'-rangeslider traj-slider', children = [
                html.Div(style={'float': 'left', 'textAlign': 'center', 'width': '50px', 'fontSize': str(CH_SIZE)+'px'}, children = [
                    html.Span(T.T), 
                    html.Br(),
                    html.Strong(T.label),
                ]),
                html.Div(style={'marginLeft': '50px'}, children = [dcc.RangeSlider(
#                    marks={i: {'label':'p'+str(i)} for i in range(T.size)}, # , 'style':{'display': 'block'}
                    marks=dict(map(lambda i: (i, {'label':T.points[i].p}), range(T.size))),
                    min=0,
                    max=T.size-1,
                    value=[0, T.size-1],
    #                 disabled=True,
                )]),
            ], style={'width': getAttrCHS(T.size, size)}))
            
            def getAttrLine(attr):
                def add_vals(m):
#                for m in ls_movs:
                    if m.trajectory.tid == T.tid and T.attribute_names[attr] in m.attribute_names:
#                        values += [m.start, m.start+m.size]
                        return [m.start, m.start+m.size-1]
                    return []
                values = sum(map(lambda m: add_vals(m), ls_movs), [])
    
                a_name = T.attributes[attr].text
                return html.Div(
                    className='traj-color'+str((k % ncor) + 1)+'-rangeslider traj-slider traj-slider', children = [
                    html.A(a_name, style={'float': 'left', 'textAlign': 'center', 'width': '50px', 'fontSize': str(CH_SIZE)+'px'}),
                    html.Div(style={'marginLeft': '50px'}, children = [dcc.RangeSlider(
#                        marks={i: str(T.points[i].aspects[attr].value) for i in range(T.size)}, # , 'style':{'display': 'block'}
                        marks=dict(map(lambda i: (i, str(T.points[i].aspects[attr])) , range(T.size) )),
                        min=0,
                        max=T.size-1,
#                             value=[0, T.size-1],
                        value=list(set(values)),
                        disabled=True,
                    )]),
                ], style={'width': getAttrCHS(T.size, size)})#)
            ls_components = ls_components + list(map(lambda attr: getAttrLine(int(attr)), sel_attributes))
            ls_components.append(html.Hr())
        list(map(lambda k: renderT(k), tqdm(range(len(ls_trajs)), desc='Rendering Trajectories')))
#    else:
#        ls_components.append(render_mat_filter(ls_trajs, from_trajs, to_trajs, [], []))
    
    return html.Div(ls_components)

def render_mat_movelets(T, ls_movs):
    ls_components = []
    attributes = T.attributes
    size = SIZE #getAttrSize(T, attributes)

    ls_components.append(html.Div(children = [
        html.Div(style={'float': 'left', 'textAlign': 'center', 'width': '50px', 'fontSize': str(CH_SIZE)+'px'}, children = [
            html.Span(T.tid), 
            html.Br(),
            html.Strong(T.label),
        ]),
        html.Div(style={'marginLeft': '50px'}, children = [dcc.RangeSlider(
#            marks={i: {'label':'p'+str(i)} for i in range(T.size)}, # , 'style':{'display': 'block'}
            marks=dict(map(lambda i: (i, {'label':T.points[i].p}), range(T.size))), 
            min=0,
            max=T.size-1,
            value=[0, T.size-1],
        )]),
    ], style={'width': getAttrCHS(T.size, size)}))
    ls_components.append(html.Hr())
    
    def renderM(m):
        nonlocal ls_components, T
        
        if m.trajectory.tid == T.tid:        
            ls_components.append(html.H6(m.Miq))
            ls_components += list(map(lambda attr: html.Div(children = [
                    html.A(T.attributes[attr].text, 
                           style={'float': 'left', 'textAlign': 'center', 'width': '50px', 'fontSize': str(CH_SIZE)+'px'}),
                    html.Div(style={'marginLeft': '50px'}, children = [dcc.RangeSlider(
#                        marks={i: str(T.points[i].aspects[attr].value) for i in range(T.size)}, # , 'style':{'display': 'block'}
                        marks=dict(map(lambda i: (i, str(T.points[i].aspects[attr])) , range(T.size) )),
                        min=0,
                        max=T.size-1,
                        value=[m.start, m.start+m.size-1],
                        tooltip={"placement": "bottom", "always_visible": False},
                    )]),
                ], style={'width': getAttrCHS(T.size, size)}), m._attributes))
            ls_components.append(html.Hr())
    list(map(lambda m: renderM(m), ls_movs))
    
    return html.Div(ls_components)

# ------------------------------------------------------------
CH_SIZE = 10
SIZE = 10 # temporary
def getAttrCHS(length, size):
    return str(length*size+length*3)+'ch' #str(length*size*(CH_SIZE/2)+length*(CH_SIZE/2)*3)+'px'

def getAttrSize(T, sel_attributes):
    if len(sel_attributes) <= 0:
        idx = list(range(len(T.attributes))) #idx = names2indexes(sel_attributes, T.attributes)
    else:
        idx = sel_attributes

    return max( list(map(lambda i: max( 
        list(map(lambda j: len(str(T.points[i].aspects[j])), idx)) 
    ), range(T.size))) )

# ------------------------------------------------------------
def getSelection(ls_trajs, sel_attributes):
    if len(ls_trajs) > 0:
        attributes = ls_trajs[0].attributes
        
        if sel_attributes == '' or sel_attributes is None:
            sel_attributes = list(range(min(10, len(attributes))))
        else:
            sel_attributes = sel_attributes if isinstance(sel_attributes, list) else sel_attributes.split(',')
        return attributes, sel_attributes
    else:
        return [], []