import os
import pandas as pd

import base64
from datetime import datetime, date
import io

import dash
from dash import dash_table
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from matplotlib import pyplot as plt
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from matview.web.app_base import app, sess, gess
from matview.web.config import WEB_ROUTE, RESULTS_FILE, render_markdown_file, alert, underDev

from matview.util.format import format_float, format_hour, findComponent
from matview.web.definitions import *
from matview.plot import MODULE_NAMES, importPlotter

from matview.scripting.component._base import BaseMethod

def render(pathname):
    sess('DATA', None)
    content = []
    content = render_experiments()
    
    return html.Div(children=[
        render_markdown_file(WEB_ROUTE+'/result/results.md', div=True),
        html.Div(id='content-result', children=content)
    ])

def render_method(pathname):
    return [underDev(pathname)]
    
# --- --- --- --- --- --- CALBACKS --- --- --- --- --- --- 
@app.callback(
    Output(component_id='content-result', component_property='children'),
    Input('input-results-datasets', 'value'),
    Input('input-results-methods', 'value'),
    Input('input-results-models', 'value'),
    Input('input-results-columns', 'value'),
    Input('input-results-view', 'value'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'),
)
def render_experiments_call(sel_datasets=None, sel_methods=None, sel_models=None, sel_columns=[], view='bar',
                            contents=None, filename=None, fdate=None):
    
    if contents is not None:
        DATA = gess('DATA')
    
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                decoded = io.StringIO(decoded.decode('utf-8'))
                DATA = [pd.read_csv(decoded), filename, datetime.fromtimestamp(fdate)]
                sess('DATA', DATA)
                return render_experiments(None, None, None, [], view)
            else:
                return [dbc.Alert("File format invalid (use CSV exported with 'automatise.results.history').", color="danger", style = {'margin':'1rem'})] + \
                    render_experiments(None, None, None, [], view)
        except Exception as e:
            print(e)
            return [dbc.Alert("There was an error processing this file.", color="danger", style = {'margin':'1rem'})] + \
                    render_experiments(None, None, None, [], view)
    
    return render_experiments(sel_datasets, sel_methods, sel_models, sel_columns, view)

@app.callback(
    Output("download-results-csv", "data"),
    Input("download-results-btn", "n_clicks"),
    State('input-results-datasets', 'value'),
    State('input-results-methods', 'value'),
    State('input-results-models', 'value'),
    prevent_initial_call=True,
)
def download_results_csv(n_clicks, sel_datasets=None, sel_methods=None, sel_models=None):
    df, *x = filter_results(sel_datasets, sel_methods, sel_models, RESULTS_FILE)
    return dcc.send_data_frame(df.to_csv, "filtered_experimental_history.csv")


# --- --- --- --- --- --- FILTER --- --- --- --- --- --- 
def filter_results(sel_datasets=None, sel_methods=None, sel_models=None, file=RESULTS_FILE):
    DATA = gess('DATA')

    time = date.today()
    if DATA:
        df = DATA[0].copy()
        time = DATA[2]
    else:
        df = pd.read_csv(file, index_col=0)
        time = datetime.fromtimestamp(os.path.getmtime(file))
        
#    columns = list(filter(lambda col: col.startswith('metric:') or col in ['totaltime', 'cls_runtime', 'candidates', 'movelets'], df.columns))
#    sel_columns = list(filter(lambda col: col in sel_columns, df.columns))
    
    df['set'] = df['dataset'] + list(map(lambda ss: ' ('+ss+')' if ss != 'specific' else '', df['subset']))
    
#    def get_sort_methods(df):
#        methods = list(df['method'].unique())
#        aux = list(filter(lambda x: x not in METHOD_NAMES.keys(), methods))
#        aux.sort()
#        methods = list(filter(lambda x: x in methods, METHOD_NAMES.keys())) + aux
#        return methods
    
    datasets    = list(df['set'].unique())
    methods     = list(df['method'].unique()) #get_sort_methods(df)
    models      = list(df['model'].unique())
    names       = list(df['name'].unique())
    dskeys      = list(df['key'].unique())
    
    if sel_datasets == None or sel_datasets == []:
        sel_datasets = datasets
    if sel_methods == None or sel_methods == []:
        sel_methods = methods
    if sel_models == None or sel_models == []:
        sel_models = models

    f1 = df['set'].isin(sel_datasets)
    f2 = df['method'].isin(sel_methods)
    f3 = df['model'].isin(sel_models)
#    f4 = df['name'].isin(names)
#    f5 = df['key'].isin(dskeys)
    df = df[f1 & f2 & f3]# & f4 & f5]
                   
    return df, DATA, time, datasets, methods, models, names, dskeys, sel_datasets, sel_methods, sel_models

# --- --- --- --- --- --- RENDERS --- --- --- --- --- --- # DEFAULT: bar_mean
def render_experiments(sel_datasets=None, sel_methods=None, sel_models=None, sel_columns=[], view='bar_mean', file=RESULTS_FILE):
    
    df, DATA, time, datasets, methods, models, names, dskeys, sel_datasets, sel_methods, sel_models = \
        filter_results(sel_datasets, sel_methods, sel_models, file)
    
    columns = list(filter(lambda col: col.startswith('metric:'), df.columns))
    if (not sel_columns or len(sel_columns) <= 0) and len(columns) > 0:
        sel_columns = [columns[0]] # select fisrt metric
    
    return [
        html.Div([
            html.Div([
                html.Div([
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Visualizing '+DATA[1] if DATA else 'Provide results in CSV file',
                            html.A(' (Drag and Drop or Select Files)')
                        ]),
                        style={
                            'height': '50px',
                            'lineHeight': '50px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '5px'
                        },
                        # Allow multiple files to be uploaded
                        multiple=False
                    ),
                    html.Strong('Metrics: '),
                    dcc.Dropdown(
                        id='input-results-columns',
                        options=list(map(lambda x: {'label': metricName(x), 'value': x}, columns)),
                        multi=True,
                        value=sel_columns,
                        style = {'width':'100%'},
                    ),
                    html.Strong('Visualization Model: '),
                    dcc.Dropdown(
                        id='input-results-view',
#                        options=[
#                            {'label': ' '+y+' ', 'value': y.lower().replace(' ', '_')} \
#                            for y in ['Critical Difference', 'Bar Plots', 'Bar Plots (Mean)', 'Box Plots', 'Swarm Plots', 'Average Rankings', 'Raw Results']
#                        ], #TODO  'Pivot Table',
                        options=list(map(lambda kv:
                            {'label': ' '+kv[1]+' ', 'value': kv[0]}, MODULE_NAMES.items()
                        )) + [
                            {'label': ' Average Rankings ', 'value': 'average_rank'},
#                            {'label': ' Pivot Table ', 'value': 'pivot_table'},
                            {'label': ' Raw Results ', 'value': 'raw_results'},
                        ],
                        value=view,
                    ),
                ], style={'width': '50%', 'flex': 1}),
                html.Div([
                    html.Strong('Datasets: '),
                    dcc.Dropdown(
                        id='input-results-datasets',
#                        options=[
#                            {'label': x, 'value': x} for x in datasets
#                        ],
                        options=list(map(lambda x: {'label': x, 'value': x}, datasets)),
                        multi=True,
                        value=sel_datasets,
                        style = {'width':'100%'},
                    ),
                    html.Strong('Models: '),
                    dcc.Dropdown(
                        id='input-results-models',
#                        options=[
#                            {'label': CLASSIFIERS_NAMES[x] if x in CLASSIFIERS_NAMES.keys() else x, 
#                             'value': x} for x in classifiers
#                        ],
                        options=list(map(lambda x: 
                            {'label': MODEL_NAMES[x] if x in MODEL_NAMES.keys() else x, 
                             'value': x}, models
                        )),
                        multi=True,
                        value=sel_models,
                        style = {'width':'100%'},
                    ),
                    html.Strong('Methods: '),
                    dcc.Dropdown(
                        id='input-results-methods',
#                        options=[
#                            {'label': METHODS_NAMES[x] if x in METHODS_NAMES.keys() else x, 
#                             'value': x} for x in methods
#                        ],
                        options=list(map(lambda x: 
#                            {'label': METHOD_NAMES[x] if x in METHOD_NAMES.keys() else x, 
                            {'label': getMethodName(x), 
                             'value': x}, methods
                        )),
                        multi=True,
                        value=sel_methods,
                        style = {'width':'100%'},
                    ),
                ], style={'width': '50%', 'marginLeft': '1rem', 'flex': 1}),
            ], style={'display': 'flex', 'flexDirection': 'row'}),
#            html.Div([
#            ]),
        ], style={'margin': '1rem'}),
        html.Hr(),
        render_result_panel(df, view, sel_methods, sel_datasets, sel_models, sel_columns),
        html.Br(),
        html.Span("Last Update: " + time.strftime("%d/%m/%Y, %H:%M:%S"), style={'margin':10}),
        dbc.Button("download results", id="download-results-btn", color="light"),
        dcc.Download(id="download-results-csv"),
        html.Br(), html.Br(),
    ]

def render_result_panel(df, view, sel_methods=None, sel_datasets=None, sel_models=None, sel_columns=[]):
    plt.close('all')
    
    if view in MODULE_NAMES.keys():
        content = render_plot(df, sel_methods, sel_datasets, sel_models, sel_columns, view)
    elif view == 'average_rank':
        content = render_ranks(df.copy(), sel_columns)
    elif view == 'pivot_table':
        content = render_expe_pivot_table(df.copy(), sel_methods, sel_datasets)
    else: #elif view == 'raw_results':
        content = render_expe_table(df.copy())
        
    return html.Div(id="results-tabs", children=content, style={'margin': '1rem'})
    
#    if view == 'critical_difference':
#        return html.Div(id="results-tabs", children=[render_expe_graph(df.copy())], style={'margin':10})
#    elif view == 'box_plots':
#        return html.Div(id="results-tabs", children=[render_expe_boxplots(df.copy(), sel_methods, plot_type='box')], style={'margin':10})
#    elif view == 'swarm_plots':
#        return html.Div(id="results-tabs", children=[render_expe_boxplots(df.copy(), sel_methods, plot_type='swarm')], style={'margin':10})
#    elif view == 'bar_plots':
#        return html.Div(id="results-tabs", children=[render_expe_barplot(df.copy(), sel_methods, sel_datasets, aggregate_ds=False)], style={'margin':10})
#    elif view == 'bar_plots_(mean)':
#        return html.Div(id="results-tabs", children=[render_expe_barplot(df.copy(), sel_methods, sel_datasets, aggregate_ds=True)], style={'margin':10})
#    elif view == 'line_rank':
#        return html.Div(id="results-tabs", children=[render_expe_linerank(df.copy(), sel_methods, plot_type='linerank')], style={'margin':10})
#    elif view == 'average_rankings':
#        return html.Div(id="results-tabs", children=[render_ranks(df.copy())], style={'margin':10})
#    elif view == 'pivot_table':
#        return html.Div(id="results-tabs", children=[render_expe_pivot_table(df.copy(), sel_methods, sel_datasets)], style={'margin':10})
#    else: #elif view == 'raw_results':
#        return html.Div(id="results-tabs", children=[render_expe_table(df.copy())], style={'margin':10})
    

# --- --- --- --- --- --- PLOT --- --- --- --- --- --- 
def render_plot(df, sel_methods, sel_datasets, sel_models, sel_columns, plot_name):    
    
    plot_function = importPlotter(plot_name)
    
#    columns = list(filter(lambda col: col.startswith('metric:') or col in ['totaltime', 'cls_runtime', 'candidates', 'movelets'], df.columns))

    def createFig(col, data):
        metric = metricName(col)

        try:
            fig = plot_function(data, col, 
                                methods_order=sel_methods, 
                                datasets_order=sel_datasets,
                                models_order=sel_models,
                               ) #, xaxis_format=xaxis_format)#, plot_type=plot_type)
            buf = io.BytesIO()
            fig.savefig(buf, bbox_inches='tight', format = "png") # save to the above file object

            fig = base64.b64encode(buf.getbuffer()).decode("utf8")
            return html.Div(html.Img(src="data:image/png;base64,{}".format(fig)), style={'padding':'1rem'})
        except Exception as e:
            print(metric, 'results not possible: ', type(e), str(e), vars(e))
            return alert(metric + ' Plot not possible with these parameters, ' + str(e))
    
    plots = list(map(lambda col: createFig(col, df.copy()), sel_columns))
    return plots


# --- --- --- --- --- --- Other Views --- --- --- --- --- --- 
def render_ranks(df, sel_columns):
    components = []

    for col in sel_columns:
        if 'time' in col: # Fix for time columns
            components += [
                html.H4(metricName(col)+' Ranks:'),
                render_avg_rank(df[df[col] > 0], rank_col=col, ascending=True, format_func=format_hour),
                html.Hr(), html.Br(),
            ]
        else:
            components += [
                html.H4(metricName(col)+' Ranks:'),
                render_avg_rank(df, rank_col=col, ascending=False),
                html.Hr(), html.Br(),
            ]
    return html.Div(components, style={'margin':'1em'})
#    [
#        html.H4('Accuracy Ranks:'),
#        render_avg_rank(df, rank_col='metric:accuracy', ascending=False),
#        html.Hr(), html.Br(),
#        html.H4('Total Time Ranks:'),
#        render_avg_rank(df, rank_col='metric:totaltime', ascending=True, format_func=format_hour),
#        html.Hr(), html.Br(),
#        html.H4('Classification Time Ranks:'),
#        render_avg_rank(df[df['cls_runtime'] > 0], rank_col='cls_runtime', ascending=True, format_func=format_hour),
#        html.Br(),
#    ], style={'margin':10})

def render_avg_rank(df, rank_col='metric:accuracy', ascending=False, format_func=format_float): 
    cls_name = 'method'
    ds_key = 'key'
    
    components = [html.Br()]
    
    for dataset in df['dataset'].unique():
        dfx = pd.DataFrame(df[df['dataset'] == dataset])
        dfx['rank'] = dfx[rank_col].rank(ascending=ascending)
        dfx = dfx.groupby([cls_name, 'model']).mean(['rank'])
        dfx = dfx.sort_values(['rank']).reset_index()

        rankItems = []
        value = None
        rank = 0
        for i in range(len(dfx)):
            rank = rank+1 if value != dfx[rank_col][i] else rank # Share the same position
            value = dfx[rank_col][i]
            rankItems.append(dbc.ListGroupItem(
                dbc.Row(
                    [ #                    str(i+1)
                        dbc.Col(dbc.Badge('{:.0f}º'.format(rank), color="light", text_color="primary", className="ms-1")),
#                        dbc.Col(html.Span( METHOD_NAMES[dfx[cls_name][i]] 
#                                          if dfx[cls_name][i] in METHOD_NAMES.keys() else dfx[cls_name][i] )),
                        dbc.Col(html.Span( getMethodName(dfx[cls_name][i]) )),
                        dbc.Col(html.Span( MODEL_NAMES[dfx['model'][i]] 
                                          if dfx['model'][i] in MODEL_NAMES.keys() else dfx['model'][i] )),
                        dbc.Col(html.Span( format_func(value) )),
                        dbc.Col(html.Span(str(dfx['rank'][i]) + ' (Avg Rank)')),
                    ]
                ),
                color="info" if i==0 else "light", style={'width': 'auto'}))
            
        components.append(html.H6(dataset+':'))
        components.append(dbc.ListGroup(rankItems))
        components.append(html.Br())
    
    return html.Div(components)#, style={'margin':10})

def render_expe_table(df):
    
    dfx = df.drop(['#','timestamp','file','random','set','error','name','key'], axis=1, errors='ignore')
    
#    dfx['method'] = [METHOD_NAMES[x] if x in METHOD_NAMES.keys() else x for x in dfx['method']]
    dfx['method'] = [getMethodName(x) for x in dfx['method']]
    
    for col in dfx.columns:
        if 'time' in col: # Fix for time columns
            dfx[col] =  dfx[col].apply(format_hour)#  [format_hour(x) for x in dfx[col]]
#    dfx['runtime'] = [format_hour(x) for x in dfx['runtime']]
#    dfx['cls_runtime'] = [format_hour(x) for x in dfx['cls_runtime']]
#    dfx['totaltime'] = [format_hour(x) for x in dfx['totaltime']]
    
    return html.Div([
        dash_table.DataTable(
            id='table-results',
            columns=[{"name": i.replace('_', ' ').title(), "id": i} for i in dfx.columns],
            data=dfx.to_dict('records'),
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
        )
    ], style={'margin': '1rem'})

def render_expe_pivot_table(df, sel_methods=None, sel_datasets=None):
    
    dfx = resultsTable(df, 'metric:accuracy', sel_methods, sel_datasets)
    
    return html.Div([
        dash_table.DataTable(
            id='table-pivot-results',
            columns=[{"name": i.replace('_', ' ').title(), "id": i} for i in dfx.columns],
            data=dfx.to_dict('records'),
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
        )
    ], style={'margin': '1rem'})

# -----------------------------------------------------------------------
def resultsTable(df, col, title='', methods_order=None, datasets_order=None): # TODO
    n = len(df)
    df.drop(df[df['error'] == True].index, inplace=True)
    print('[WARN PivotTable:] Removed results due to run errors:', n - len(df))

    if not methods_order:
        methods_order = list(df['method'].unique())
        
    if not datasets_order:
        datasets_order = list(df['dataset'].unique())
        datasets_order.sort()

#    df['methodi'] = df['method'].apply(lambda x: {methods_order[i]:i for i in range(len(methods_order))}[x])
    
    df['key'] = df['dataset']+'-'+df['subset']
#    df['dsi'] = df['key'].apply(lambda x: {datasets_order[i]:i for i in range(len(datasets_order))}[x])
#    df = df.sort_values(['methodi', 'dsi'])

#    df['method'] = list(map(lambda m: METHOD_NAMES[m] if m in METHOD_NAMES.keys() else m, df['method']))
    df['method'] = list(map(lambda m: getMethodName(m), df['method']))

    if len(set(df['model'].unique()) - set('-')) > 1:
        df['name'] = df['method'] + list(map(lambda x: '-'+x if x != '-' else '', df['model']))
    else:
        df['name'] = df['method']
        
    return pd.pivot_table(df, values='metric:accuracy', index='key', columns=['name'], fill_value='-')

# -----------------------------------------------------------------------
METHOD_COMPONENTS = BaseMethod.providedMethods()
def getMethodName(method):
    c = findComponent(method, METHOD_COMPONENTS)
    if c:
        name = c.decodeName(method)
        if method in c.NAMES.keys():
            name = c.NAMES[method] 
        else:
            name = c.decodeName(method)
        return name + ' ({})'.format(method) if name != method else name
    return method