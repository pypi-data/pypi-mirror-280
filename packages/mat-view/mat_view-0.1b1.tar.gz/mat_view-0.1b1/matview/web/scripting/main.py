import os
import pandas as pd

import base64
from datetime import datetime, date
import io

import dash
from dash import dash_table
from dash import dcc
from dash import html, callback_context, MATCH, ALL
import plotly.graph_objects as go
import plotly.express as px
from matplotlib import pyplot as plt
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

import tempfile

from matview.web.app_base import app, sess, gess
from matview.web.config import WEB_ROUTE, RESULTS_FILE, render_markdown_file, alert, underDev
from matview.web.definitions import *

from matview.web.dataset.main import list_datasets_dict

from matview.scripting.generator import gen_env, prepare_zip
from matview.scripting.component import *

#all_datasets = list_datasets()
#all_methods = ['hiper']
all_methods = BaseMethod.providedMethods()

def render(pathname):
    all_datasets = sum(map(lambda x: list(map(lambda y: x[0]+'.'+y, x[1].keys())), list_datasets_dict().items()), [])

    content = []
    return html.Div(children=[
        render_markdown_file(WEB_ROUTE+'/scripting/scripting.md'),
        
        html.Div([
            html.Div(children=[
#                html.Strong('Installation Root Path:'),
#                dbc.Input(id='input-exp-root', value='', type='text', placeholder='e.g. /home/user/experiments (or leave blank for relative path)', style={'width': '100%'}),
                
                html.Strong('Experiment Group Folder:'),
                dbc.Input(id='input-exp-folder', value='EX_01', type='text', style={'width': '100%'}),
                
                html.Br(),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(dbc.Checkbox(id='input-exp-use-dataset', value=False)), 
                        dbc.InputGroupText('Alternative Datasets Path:'),
                        dbc.Input(id='input-exp-datafolder', value='', placeholder='/home/user/experiment/data', type='text'),
                    ],
                    className="mb-3",
                ),
                
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(dbc.Checkbox(id='input-exp-use-tc', value=True)), 
                        dbc.InputGroupText('Set a Timeout: '),
                        dbc.Input(id='input-exp-tc', type="number", min=0, step=1, value=7),
                        dbc.InputGroupText(dbc.InputGroup(
                            [
                                dcc.RadioItems(
                                    id='input-exp-tccode',
                                    options=[
                                        {'label': ' '+y+' ', 'value': y[0].lower()} \
                                        for y in ['Minutes', 'Hours', 'Days', 'Weeks']
                                    ],
                                    value='d',
                                    inputStyle={'marginRight': '5px'},
                                    labelStyle={'marginLeft': '1rem', 'display': 'inline-flex'},
                                ),

                            ],
                        ))
                    ],
                    className="mb-3", style={'width': '100%', 'display': 'inline-flex'}
                ),
                
                html.Br(),
                html.Strong('Select Datasets:'),
                dcc.Dropdown(
                        id='input-exp-datasets', 
                        options=[
                            {'label': x, 'value': x} for x in all_datasets
                        ],
                        multi=True,
                        placeholder='Select repository datasets (need manual download)',
                ),
                html.Strong('Type Datasets:'),
                dbc.Input(id='input-exp-type-datasets', value='', placeholder='Or, dataset folders (comma separated): Dataset1,Dataset2', type='text', style={'width': '100%'}),
                
            ], style={'padding': 10, 'flex': 1}),

            html.Div(children=[
                html.Strong('Other Options:'),

                dbc.Checkbox(id='input-exp-use-exe', label='Include methods executable', value=True),
                
                dbc.InputGroup(
                    [
                        dbc.InputGroupText('# of Threads:'), 
                        dbc.Input(id='input-exp-nt', type="number", min=0, step=1, value=4),
                        dbc.InputGroupText('Mem. Limit:'),
                        dbc.Input(id='input-exp-gb', type="number", min=0, step=1, value=600),
                        dbc.InputGroupText('GB'), 
                    ],
                    className="mb-3",
                ),
                
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(dbc.Checkbox(value=False, id='input-exp-is-k')), 
                        dbc.InputGroupText('K-Fold:'),
                        dbc.Input(id='input-exp-k', type="number", min=1, step=1, value=5),
                        dbc.InputGroupText('resamples'),
                    ],
                    className="mb-3",
                ),
                
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(dbc.Checkbox(value=True)), 
                        dbc.InputGroupText('Python command:'),
                        dbc.Input(id='input-exp-pyname', value='python3', type='text'),
                    ],
                    className="mb-3",
                ),
                
                html.Br(),
                
                html.Strong('Select Methods:'),
                dbc.InputGroup(
                    [
                        dbc.Select(
                            id='input-experiments-methods',
                            options=[
                                {'label': v.NAMES[k], 'value': k} for k,v in all_methods.items()
                            ],
                            value=list(all_methods.keys())[0]
                        ),
                        dbc.Button('Add Method', outline=True, color="success", id='experiments-method-add'), 
                    ],

                ),
                html.Br(),
                html.Br(),
                
                dbc.Button('Reset', id='experiments-reset', style={'float': 'left'}, outline=True, color="warning"),
                dbc.Button('Download Environment', id='experiments-download', style={'float': 'right'}),
                
            ], style={'padding': 10, 'flex': 1})
        ], style={'display': 'flex', 'flexDirection': 'row'}),
        
        dcc.Download(id="download-experiments"),
        dbc.Alert('Configure the environment, select datasets, and add methods to your experiments. Then, click Download Environment to generate script files and folders.', id="experiments-err", color='secondary', style = {'margin':10}),
        html.Hr(),
        dbc.Accordion(id='experiments-methods-container', children=[]),
        html.Div(id='output-experiments', children=content),
        html.Br(),
        html.Br(),
    ], style={'margin': '1rem'})

# --------------------------------------------------------------------------------
# Methods add:
MLIST = []

@app.callback(
    Output('experiments-methods-container', 'children'),
    Input('experiments-method-add', 'n_clicks'),
    State('input-experiments-methods', 'value'),
    State('experiments-methods-container', 'children'),
    Input('experiments-reset', 'n_clicks'),
    prevent_initial_call=True,
)
def display_methods(idx, method, children, reset):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    
    if 'experiments-reset' in changed_id:
        return reset_methods()
    
    idx = len(MLIST) + 1
    
    generator = all_methods[method](idx)
    
    MLIST.append(generator)
    
    item = dbc.AccordionItem(
        generator.render(),
        title=getTitle(idx-1),#generator.title(),
        id={
            'type': 'exp-container',
            'index': idx
        },
    )
    children.append(item)
    return children

def reset_methods():
    global MLIST
    MLIST = []
    return []

# --------------------------------------------------------------------------------
### PARAM 1 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param1', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p1(id, value): 
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0] 
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=1)
    return getTitle(idx)

### PARAM 2 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param2', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p2(id, value): 
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=2)
    return getTitle(idx)


### PARAM 3 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param3', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p3(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=3)
    return getTitle(idx)

### PARAM 4 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param4', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p4(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=4)
    return getTitle(idx)

### PARAM 5 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param5', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p5(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=5)
    return getTitle(idx)

### PARAM 6 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param6', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p6(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=6)
    return getTitle(idx)

### PARAM 7 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param7', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p7(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=7)
    return getTitle(idx)

### PARAM 8 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param8', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p8(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=8)
    return getTitle(idx)

### PARAM 9 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param9', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p9(id, value):
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=9)
    return getTitle(idx)

### PARAM 10 ###
@app.callback(
    Output({'type': 'exp-container', 'index': MATCH}, 'title', allow_duplicate=True),
    State({'type':  'exp-container', 'index': MATCH}, 'id'),
    
    Input({'type': 'exp-param10', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def update_p10(id, value): 
    global MLIST
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]   
    idx = id['index']-1
    
    MLIST[idx].update(changed_id, value, param_id=10)
    return getTitle(idx)


def getTitle(idx):
    global MLIST
    return str(idx+1)+') ' + MLIST[idx].title()

# --------------------------------------------------------------------------------
# DOWNLOAD:
@app.callback(
    Output('download-experiments', 'data'),
    Output('experiments-err', 'children'),
    Input('experiments-download', 'n_clicks'),
#    State('input-exp-root', 'value'),
    State('input-exp-folder', 'value'),
    State('input-exp-use-dataset', 'value'),
    State('input-exp-datafolder', 'value'),
    State('input-exp-use-tc', 'value'),
    State('input-exp-tc', 'value'),
    State('input-exp-tccode', 'value'),
    State('input-exp-datasets', 'value'),
    State('input-exp-type-datasets', 'value'),
    State('input-exp-use-exe', 'value'),
    State('input-exp-nt', 'value'),
    State('input-exp-gb', 'value'),
    State('input-exp-is-k', 'value'),
    State('input-exp-k', 'value'),
    State('input-exp-pyname', 'value'),
    prevent_initial_call=True,
)
def download(value, basedir, isDs, datapath, isTC, TC, TCD, datasets, otherds, isExe, nt, gb, isk, k, pyname):
    global MLIST
    
    if not datasets and not otherds:
        return dash.no_update, 'You must specify at least one dataset.'
    if len(MLIST) <= 0:
        return dash.no_update, 'You must add methods to generate scripts.'
    
    if not isk:
        k = False
        
    if otherds and not otherds == '':
        otherds = otherds.split(',')
    else:
        otherds = []
        
    envdir = tempfile.TemporaryDirectory()
    
    gen_env(envdir.name, MLIST, basedir, datapath, datasets, otherds, isDs, isTC, TC, TCD, nt, gb, k, pyname)
    
    zf_tf = tempfile.NamedTemporaryFile(delete=True, suffix='.zip')
    prepare_zip(envdir.name, zf_tf)
    
    def close_tmp_file(tf):
        try:
            os.unlink(tf.name)
            tf.close()
        except:
            pass
        
    close_tmp_file(envdir)
    
    return dcc.send_file(zf_tf.name, filename="experimental_env.zip"), 'Files generated to "experimental_env.zip"'