# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2021
Copyright (C) 2021+, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
'''
import pandas as pd
import numpy as np
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

from tqdm.auto import tqdm

from pandas import json_normalize

from matdata.preprocess import readDataset, organizeFrame
from matdata.converter import csv2df, read_zip #, read_mat, load_from_tsfile, xes2df

from matmodel.util.parsers import df2trajectory, json2movelet

from matview.web.app_base import app, sess, gess

from matview.web.view.mat import render_mat, render_mat_filter, render_mat_movelets, getSelection
from matview.web.view.graph import render_graph, render_graph_filter
from matview.util.stats import *
# ------------------------------------------------------------
@app.callback(
    Output('output-data-upload', 'children'), 
#    Output('filter-mat', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'),
    State('output-data-upload', 'children'),
    State('input-range-mats', 'value'),
    State('input-attr-traj', 'value'),
    running=[(Output("load-screen", "style"), {'visibility': 'visible'}, {'visibility': 'hidden'})],
#    prevent_initial_call=True
)
def update_statistic(list_of_contents, list_of_names, list_of_dates, components, range_value, sel_attributes):
    ls_tids        = set(gess('ls_tids', []))
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
    
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        
        return html.Div(render_statistics(ls_tids, ls_trajs, ls_movs))

@app.callback(
    Output('filter-mat', 'children'),
    Input('output-data-upload', 'children'),
    State('input-range-mats', 'value'),
    State('input-attr-traj', 'value'),
#    prevent_initial_call=True,
)
def update_mat_filter(state_change, range_value, sel_attributes):
    ls_trajs       = gess('ls_trajs', [])
    from_trajs, to_trajs = range_value
    attributes, sel_attributes = getSelection(ls_trajs, sel_attributes)
    return render_mat_filter(ls_trajs, from_trajs, to_trajs, attributes, sel_attributes)

@app.callback(
    Output('filter-graph', 'children'),
    Input('output-data-upload', 'children'),
    Input('input-range-mov-graph', 'value'),
    Input('input-attr-mov-graph', 'value'),
    Input('input-format-mov-graph', 'value'),
#    prevent_initial_call=True,
)
def update_graph_filter(state_change, range_value, sel_attributes, model):
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
    from_value, to_value = range_value
    
    attributes = []
    if len(ls_trajs) > 0:
        attributes = ls_trajs[0].attributes
    elif len(ls_movs) > 0:
        attributes = dict(map(lambda item: (item.text, item), 
                              sum(map(lambda m: m.attributes, ls_movs), []) # flattening
                             )) 
        #list(set([x['text'] for m in ls_movs for x in m.attributes]))
        attributes = sorted(attributes.values(), key=lambda d: d.order)
    
    return render_graph_filter(ls_movs, model, from_value, to_value, attributes, sel_attributes)
    
@app.callback(
    Output(component_id='output-mats', component_property='children'),
    Input(component_id='output-data-upload', component_property='children'),
#     Input('input-from-traj', 'value'),
#     Input('input-to-traj', 'value'),
    Input('input-range-mats', 'value'),
    Input('input-attr-traj', 'value'),
)
def update_mat_view(input_value, range_value, sel_attributes):
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
    return render_mat(ls_trajs, range_value, ls_movs, sel_attributes)
    
@app.callback(
    Output(component_id='output-mat-movelet', component_property='children'),
    Input('input-traj', 'value'),
)
def update_matmov_view(input_value):
#     global sel_traj, ls_movs
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
#     sel_traj       = gess('sel_traj', '')
    
    traj = None #ls_trajs[0] if len(ls_trajs) > 0 else None
    if input_value != '':
        for T in ls_trajs:
            if str(input_value) == str(T.tid):
                traj = T
                break 
    if traj:
        return render_mat_movelets(traj, ls_movs)
    else:
        return dbc.Alert("Select a valid TID.", color="info", style = {'margin':10})


@app.callback(Output('output-graph', 'children'),
              Input('upload-data', 'contents'),
              Input('input-range-mov-graph', 'value'),
              Input('input-attr-mov-graph', 'value'),
              Input('input-format-mov-graph', 'value'),
#               Input('input-from-mov-graph', 'value'),
#               Input('input-to-mov-graph', 'value'),
)
def update_graph_view(list_of_contents, range_value, sel_attributes, model):
    
    from_trajs     = gess('from_trajs', 0)
    to_trajs       = gess('to_trajs', 100)
    
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
    
    if len(ls_movs) > 0:
        from_trajs, to_trajs = range_value
        from_trajs = int(from_trajs) if from_trajs != '' else 0
        to_trajs = int(to_trajs) if to_trajs != '' else 10
        
        sess('from_trajs', from_trajs)
        sess('to_trajs', to_trajs)

#        if len(ls_trajs) > 0:
#            attributes = ls_trajs[0].attributes
#        else:
#            attributes = list(set([x for m in ls_movs for x in m.attributes()]))
#            attributes.sort()

        return html.Div(style = {'width':'100%'}, 
            children = render_graph(ls_movs, model, from_trajs, to_trajs, sel_attributes))
    
    return render_graph(ls_movs, '', 0, 100, '')


# ------------------------------------------------------------
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    # DECODE DATAFRAME:
    decoded = base64.b64decode(content_string)
    try:
        ext = filename.split('.')[-1].lower()
        if ext in ['csv', 'zip', 'mat', 'ts']:

            df = pd.DataFrame()
            if ext == 'csv':
#                from matdata.converter import csv2df
                decoded = io.StringIO(decoded.decode('utf-8'))
                df = csv2df(decoded, missing='?')
            elif ext == 'zip':
#                from matdata.converter import read_zip
                from zipfile import ZipFile
                decoded = io.BytesIO(decoded)
                df = read_zip(ZipFile(decoded, "r"))
            elif ext == 'mat':
#                from matdata.converter import read_mat
                decoded = io.StringIO(decoded.decode('utf-8'))
                df = read_mat(decoded, missing='?')
            elif ext == 'ts':
#                from matdata.inc.ts_io import load_from_tsfile
                decoded = io.StringIO(decoded.decode('utf-8'))
                df = load_from_tsfile(decoded, replace_missing_vals_with="?")
            elif ext == 'xes':
#                from matdata.converter import xes2df
                decoded = io.StringIO(decoded.decode('utf-8'))
                df = xes2df(decoded, missing='?')

            df.columns = df.columns.astype(str)

            df, columns_order_zip, columns_order_csv = organizeFrame(df)
            update_trajectories(df[columns_order_csv])
        elif ext == 'json':
            update_movelets(io.BytesIO(decoded))
        else:
            return dbc.Alert("This file format is not accepted.", color="warning", style = {'margin':'1rem'})
    except Exception as e:
        raise e
        print(e)
        return dbc.Alert("There was an error processing this file.", color="danger", style = {'margin':'1rem'})

    return dbc.Alert("File "+filename+" loaded ("+str(datetime.datetime.fromtimestamp(date))+").", color="info", style = {'margin':'1rem'})

# ------------------------------------------------------------
def update_trajectories(df):
    # TRANSFORM TRAJECTORIES:
    ls_tids        = set(gess('ls_tids', []))
    ls_trajs       = gess('ls_trajs', [])
    
    ls_aux, _ = df2trajectory(df)
    #for T in ls_aux:
    def processT(T):
        nonlocal ls_tids, ls_trajs
        if T.tid not in ls_tids:
            ls_tids.add(T.tid)
            ls_trajs.append(T)
            
    list(map(lambda T: processT(T), ls_aux))
            
    sess('ls_tids', list(ls_tids))
    sess('ls_trajs', ls_trajs)
            
def update_movelets(data):
    # TRANSFORM Movelets:
    ls_movs       = gess('ls_movs', [])
    
    ls_aux = json2movelet(data)
    
    ls_movs = ls_movs + ls_aux 
        
    sess('ls_movs', ls_movs)


# ------------------------------------------------------------
def render_statistics(ls_tids, ls_trajs, ls_movs):
    ls_tids        = set(gess('ls_tids', []))
    ls_trajs       = gess('ls_trajs', [])
    ls_movs        = gess('ls_movs', [])
    
    # Update Screen:
    components = []
    components.append(html.Hr())
    if len(ls_movs) > 0:
        df_stats = movelet_stats(ls_movs)
        df_stats = movelet_stats_bylabel(df_stats)
        
        components.append(html.Details(style = {'margin':'1rem', 'display':'grid'}, open=True, children = 
            [
                html.Summary(
                    html.A(children=[
                        html.Strong('Total Number of Movelets: '),
                        html.Span(str(len(ls_movs))),
                    ]),
                ),
                html.Div(list(map(lambda d: 
                     html.Details(open=True, children = [
                        html.Summary([
                            html.Strong('Label: '),
                            html.Span(str(d['label'])),
                        ]),
                        html.Div(list(map(lambda x:
                            html.Div([
                                html.Strong(x[0]+': '),
                                html.Span(str(x[1])),
                            ])
                        , list(d.items())[1:])),
                        style={'textIndent':'4em'})
                     ]), df_stats.to_dict('records'))),
                    style={'textIndent':'2em'}
                )
            ]
        ))
        components.append(html.Hr())
    
    if len(ls_trajs) > 0:
        labels, samples, top, bot, npoints, avg_size, diff_size, attr, num_attr, classes = trajectory_stats(ls_trajs)
        
        ds_stats = html.Div(style = {'margin':'1rem'}, children = [
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            html.Div(style = {'margin':'1rem', 'display':'grid'}, children = [
                                html.Div(style = {'display':'inline'}, children = [
                                    html.Strong('Number of Trajectories: '),
                                    html.Span(str(samples)),
                    #                 html.Br(),
                    #                 html.Span(', '.join(['Class '+str(k)+': '+str(v) for k,v in classes.items()])),
                                ]),
                                html.Div(style = {'display':'inline'}, children = [
                                    html.Strong('Number of Labels: '),
                                    html.Span(len(classes)),
                                ]),
                                html.Div(style = {'display':'inline'}, children = [
                                    html.Strong('Attributes: '),
                                    html.Span(str(num_attr)),
                                    html.Br(),
                                    html.Span('[' + (', '.join(attr)) + ']'),
                                ]),
                                html.Div(style = {'display':'inline'}, children = [
                                    html.Strong('Trajectories Size: '),
                                    html.Span(str(avg_size) + ' | from ' + str(bot) + ' to ' + str(top) + ' | ±' + str(diff_size)),
                                ]),
                                html.Div(style = {'display':'inline'}, children = [
                                    html.Strong('Number of Points: '),
                                    html.Span(str(npoints)),
                                ]),
                            ])
                        ],
                        title="Dataset Statistics",
                    ),
                    dbc.AccordionItem(
                        [
                            html.Div(style = {'display':'inline'}, children = [
                                #html.Strong('Classes: '),
                                #html.Span(str(len(labels))),
                                #html.Br(),
                                html.Span(', '.join(labels)),
                            ]),
                        ],
                        title="Labels",
                    ),
                    dbc.AccordionItem(
                        [
                            html.Div(style = {'display':'table'}, children = [ #'display':'auto'
                                #html.Br(),
                                #html.Strong('Trajectories per Class: '),
                                #html.Br(),
                                #html.Span(', '.join(['C('+str(k)+'): '+str(v) for k,v in classes.items()])),
                                dash_table.DataTable(
                                    data=pd.DataFrame(
                                        list(map(lambda kv: [kv[0], kv[1]], classes.items())),
                                        columns=['class', 'matn']
                                    ).to_dict('records'),
                                    columns=[{"name": 'Class', "id": 'class'}, {"name": '# of MAT', "id": 'matn'}],
                                    fixed_rows={'headers': True},
                                    style_table={'height': '300px', 'overflowY': 'auto'},
                                    style_cell={
                                        'minWidth': 95, 'textAlign': 'left',
                                    }
                                    
                                ),
                            ])
                        ],
                        title="Trajectories per Label",
                    ),
                ],
            )]
        )
        components.append(ds_stats)
        components.append(html.Hr())
        
    return components