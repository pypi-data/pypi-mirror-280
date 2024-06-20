import os
import glob2 as glob
import pandas as pd

import requests
import base64
import datetime
import io

import dash
from dash import dash_table
from dash import dcc
from dash import html, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from matdata.dataset import DATASET_TYPES, SUBSET_TYPES, translateCategory

from matview.util.format import format_hour
from matview.web.definitions import *
from matview.web.app_base import app
from matview.web.config import DATA_PATH, WEB_ROUTE, RESULTS_FILE, PACKAGE_NAME, render_markdown_file, underDev

# ---------------------------------------------------------------------------------
def list_datasets():
    datasetsdict = list_datasets_dict()
    datasets = {}
    
    for category, lsds in datasetsdict.items():
        for dataset, subsets in lsds.items():
            for ss in subsets:
                if ss == 'specific':
                    datasets[category+'.'+dataset] = dataset
                elif ss == 'generic':
                    datasets[category+'.'+dataset+'?'] = dataset + ' (generic)'

    return datasets

def list_datasets_dict():
    user = "mat-analysis"
    repo = "datasets"

    url = "https://api.github.com/repos/{}/{}/git/trees/main?recursive=1".format(user, repo)
    r = requests.get(url)
    res = r.json()
    
    files = list(map(lambda file: file["path"], res["tree"]))
    desc_files = list(filter(lambda f: os.path.sep+'descriptors' in f and f[-5:] == '.json', files))
    
    datasets_dict = {}
    def create_dict(file):
        if file[-3:] == '.md' and '-stats.md' not in file and 'README' not in file:
            category = file.split(os.path.sep)[0]
            if category not in datasets_dict.keys():
                datasets_dict[category] = {}
#            mp = os.path.dirname(file).split(os.path.sep)
            name = os.path.basename(file).split('.')[0]

            datasets_dict[category][name] = list_subsets(name, category, file, desc_files)
                
        return file
    
    file = list(map(lambda file: create_dict(file), files))
        
    return datasets_dict

def list_subsets(dataset, category, file, desc_files, return_files=False):        
    subsets = set()
#    desc_files = glob.glob(os.path.join(os.path.dirname(file), '..', 'descriptors', '*.json'))
    def translate(f):
        descName = os.path.basename(f) #.split('.')[0]
        descName = translateDesc(dataset, category, descName)
        if descName:
            if f.endswith('_hp.json') and not return_files:
                subsets.add(descName)
            elif return_files:
                subsets.add(f)
        return None
                
    list(map(lambda f: translate(f), desc_files))
    
    subsets = list(subsets)
    subsets.sort()
    if 'specific' in subsets:
        subsets.remove('specific')
        subsets.insert(0, 'specific')

    return subsets
    
def translateDesc(dataset, category, descName):
    dst, dsn = descName.split('.')[0].split('_')[0:2]
    if dsn in ['allfeat', '5dims']: # am ignoring those old versions
        return False
    if category.upper() in dst.upper(): # for cases with one descriptor for all datasets
        return 'specific'
    elif dataset in dst: # for specific datasets configurations
        return dsn
    return False
# ---------------------------------------------------------------------------------
def render(pathname):
    if pathname == '/dataset':
        return html.Div(style = {'margin':10}, children=[
#             html.H3('Datasets'), 
            render_markdown_file(WEB_ROUTE+'/dataset/datasets.md'),
            html.Div(children=render_datasets()),
        ])
    else:
        return render_dataset(pathname)


def render_datasets():
    lsds = list_datasets_dict()
    components = []
    
    for category, dslist in lsds.items():
#         for dataset, subsets in dslist.items():
        components.append(html.Br())
        components.append(html.H4(DATASET_TYPES[category] + ':'))
        components.append(render_datasets_category(category, dslist))
        components.append(html.Hr())
        
    return html.Div(components)
    
def render_datasets_category(category, dsdict):    
    dsdict = dict(sorted(dsdict.items()))
    
    if len(dsdict) > 30:
        return render_datasets_category_ls(category, dsdict)
    else:
        return render_datasets_category_tb(category, dsdict)
    
def render_datasets_category_tb(category, dsdict):
    
    df = pd.DataFrame()
    for dataset, subsets in dsdict.items():
        aux = {}
        aux['Name'] = '<div class="dash-cell-value"><a href="/dataset/'+category+'/'+dataset+'" class="btn btn-link">'+dataset+'</a></div>'
        aux['Category'] = getBadges(category, dataset, subsets)
#        aux['File'] = os.path.join(data_path, category, dataset, dataset+'.md')
        aux['File'] = 'https://raw.githubusercontent.com/mat-analysis/datasets/main/{}/{}/{}.md'.format(category, dataset, dataset)
#        df = df.append(aux, ignore_index=True)
        df = pd.concat([df, pd.DataFrame(aux, index=[0])])
        
    return dash_table.DataTable(
        id='table-datasets',
        columns=[{
            'id': 'Name',
            'name': 'Dataset',
            'type': 'any',
            "presentation": "markdown",
        }, {
            'id': 'Category',
            'name': 'Category',
            'type': 'text',
            "presentation": "markdown",
        }],
        markdown_options={'link_target': '_self', 'html': True},
        data=df[df.columns[:-1]].to_dict('records'),
        css=[{'selector': 'td', 'rule': 'text-align: left !important;'},
             {'selector': 'th', 'rule': 'text-align: left !important; font-weight: bold'}
        ],
    )
    
def render_datasets_category_ls(category, dsdict):    
    return html.Div([
        html.Div(html.A(dataset,
                        href='/datasets/'+category+'/'+dataset, 
                        className="btn btn-link"), 
                 style={'display': 'inline-table'})
        for dataset, subsets in dsdict.items()
    ])

#def render_datasets_all(data_path=DATA_PATH):
#    files = glob.glob(os.path.join(data_path, '*', '*', '*.md'))
#    
#    df = pd.DataFrame()
#    
#    for f in files:
#        tmp = os.path.dirname(f).split(os.path.sep)
#        aux = {}
#        name = os.path.basename(f).split('.')[0]
#        
#        aux['Name'] = '<div class="dash-cell-value"><a href="/dataset/'+name+'" class="btn btn-link">'+name+'</a></div>'
#        
#        aux['Category'] = getBadges(f, name)
#        aux['File'] = f
#
#        df = df.append(aux, ignore_index=True)
#        
#    return dash_table.DataTable(
#        id='table-datasets',
#
#        columns=[{
#            'id': 'Name',
#            'name': 'Dataset',
#            'type': 'any',
#            "presentation": "markdown",
#        }, {
#            'id': 'Category',
#            'name': 'Category',
#            'type': 'text',
#            "presentation": "markdown",
#        }],
#        markdown_options={'link_target': '_self', 'html': True},
#        data=df[df.columns[:-1]].to_dict('records'),
#        css=[{'selector': 'td', 'rule': 'text-align: left !important;'},
#             {'selector': 'th', 'rule': 'text-align: left !important; font-weight: bold'}
#        ],
#    )

# ------------------------------------------------------------
def render_dataset(pathname):
    components = []    
    if len(pathname.split(os.path.sep)) < 4:
        return underDev(pathname)
    
    category, dataset = pathname.split(os.path.sep)[2:4]
#    file = os.path.join(data_path, category, dataset, dataset+'.md')
#    if not os.path.isfile(file):
#        return underDev(pathname)
    
    file = 'https://raw.githubusercontent.com/mat-analysis/datasets/main/{}/{}/{}.md'.format(category, dataset, dataset)
    #glob.glob(os.path.join(data_path, category, dataset, dataset+'.md'))[0]
    response = requests.get(file)
    if response.status_code == 200:
        data = response.text
        components.append(html.H3(dataset))
        components.append(dcc.Markdown(data, className='markdown'))
        
    components.append(html.A('[GitHub]', href='https://github.com/mat-analysis/datasets/tree/main/{}/{}'.format(category, dataset), className="btn btn-link", target='_blank'))
        
    file = 'https://raw.githubusercontent.com/mat-analysis/datasets/main/{}/{}/{}-stats.md'.format(category, dataset, dataset)
    #glob.glob(os.path.join(data_path, category, dataset, dataset+'-stats.md'))
    response = requests.get(file)
    if response.status_code == 200:
        data = response.text
        components.append(html.Br())
        components.append(html.Hr())
        components.append(dcc.Markdown(data, className='markdown'))
    
    components.append(html.Br())
    components.append(html.Hr())
    components.append(html.H6('Best Result:'))
#     components.append(html.Br())
    components.append(render_results(dataset))
    components.append(html.Br())
    components.append(html.Hr())
    components.append(html.H6('Related Publications:'))
#     components.append(html.Br())
    components.append(render_related_publications(dataset))
    components.append(html.Br())
    components.append(html.Hr())
#    components.append(html.H6('Download Files:'))
##     components.append(html.Br())
#    components.append(render_downloads(category, dataset))
#    components.append(dcc.Download(id="download-ds"))
    components.append(html.Br())
    
    return html.Div(components, style={'margin': '20px'})

def message(msg):
    return html.Span(msg, style={'font-style': 'italic'})

def render_results(dataset):
    
    if not os.path.exists(RESULTS_FILE):
        return message('Result file not set in application.')
    
    df = pd.read_csv(RESULTS_FILE, index_col=0)
    df = df[df['dataset'] == dataset]
    
    if len(df) <= 0:
        return message('Results not available for this dataset.')
    
    records = []
    def apline(i, key, value, df):
        line = {}
        line['Best'] = key.replace('_', ' ').title()
        
#         i = df[key].idxmin() if key != 'accuracy' else df[key].idxmax()
        line['Result'] = format_hour(df[key][i]) if key != 'metric:accuracy' else df[key][i]
        
        method = df['method'][i]
        mname = METHOD_NAMES[method] if method in METHOD_NAMES.keys() else method
        mlink = mname.split('-')[0].split(' ')[0].replace('Pivots', 'Movelets') # TODO: TEMP Fix, look for a better way
        line['Method'] = '['+mname+'](../../method/'+mlink+')'
        
        method = df['model'][i]
        method = MODEL_NAMES[method] if method in MODEL_NAMES.keys() else method
        line['model'] = method
        records.append(line)
    
    i = df['metric:accuracy'].idxmax()
    apline(i, 'metric:accuracy', df['metric:accuracy'][i], df)
    i = df['metric:runtime'].idxmin()
    apline(i, 'metric:runtime', format_hour(df['metric:runtime'][i]), df)
    i = df[df['metric:clstime'] > 0]['metric:clstime'].idxmin()
    apline(i, 'metric:clstime', format_hour(df['metric:clstime'][i]), df)
    i = df['metric:totaltime'].idxmin()
    apline(i, 'metric:totaltime', format_hour(df['metric:totaltime'][i]), df)
        
    return dash_table.DataTable(data=records, columns=[
            {"name": ' ', "id":  'Best'},
            {"name": 'Result', "id":  'Result'},
            {"name": 'Method', "id":  'Method', 'type': 'text', "presentation": "markdown",},
            {"name": 'Model', "id":  'Model'},
        ], 
        style_cell={'padding-left': '5px', 'padding-right': '5px'}, css=[{
            'selector': 'table',
            'rule': '''
                width: auto !important;
            '''
        }],
        markdown_options={'link_target': '_self',},
    )
    
#     return html.Div([
#             html.Span(method+': '),
#             html.Span(str(acc)),
# #             html.Br(),
#         ]),

def render_related_publications(dataset):
    if not os.path.exists(RESULTS_FILE):
        return message('Result file not set in application.')
    
    df = pd.read_csv(RESULTS_FILE, index_col=0)
    df = df[df['dataset'] == dataset]
    
    if len(df) <= 0:
        return message('Related publications not available for this dataset.')
    
    txt = '| Title | Authors | Year | Venue | Links | Cite |\n|:------|:--------|------|:------|:------|:----:|\n'
    
    ls = [METHOD_NAMES[x].split('-')[0] if x in METHOD_NAMES.keys() else x for x in df['method'].unique()]
#     ls = list(df['method'].unique())
    for method in set(ls):
        file = os.path.join(PACKAGE_NAME, 'web', 'method', method+'.md')
        if os.path.exists(file):
            with open(file, 'r') as f:
                line = f.read().splitlines()
                line = line[-1]
                if line.startswith('|'):
                    txt += line + '\n'

    return dcc.Markdown(txt, className='markdown')

#def render_downloads(category, dataset, data_path=DATA_PATH):
#    files = glob.glob(os.path.join(data_path, category, dataset, '*.*'))
#    descs = list_subsets(dataset, category, os.path.join(data_path, category, dataset, dataset+'.md'), True)
#    
#    ls = []
#    for f in files:
#        if not f.endswith('.md'):
#            ls.append(f)
#    
#    components = [dbc.ListGroupItem(
#            html.A(os.path.basename(x), href="javascript:void(0);", #href=dataset+'/'+os.path.basename(ls[i]), 
#                   id={
#                        'type': 'download-ds-file',
#                        'index': dataset+'/'+os.path.basename(x)
#                   },
#            )
#        ) for x in ls]
#    
#    if len(descs) > 0:
#        components = components + \
#            [dbc.ListGroupItem(
#                [
#                    html.A(os.path.basename(x), href="javascript:void(0);", #href=dataset+'/'+os.path.basename(ls[i]), 
#                       id={
#                            'type': 'download-ds-file',
#                            'index': x
#                       },
#                    ),
#                    dccBadge(dataset, category, translateDesc(dataset, category, os.path.basename(x)), {'float':'right'}),
#                ]) for x in descs]
#    
#    return dbc.ListGroup(components)

# ------------------------------------------------------------
def badgeClass(category, subset):
    return 'dataset-color-' + (category if subset in ['specific', '*'] else subset) + ('-default' if subset == category else '')

def dccBadge(dataset, category, subset, style={}):
    return dbc.Badge(translateCategory(dataset, category, subset), 
                     style=style,
                     color="primary", 
                     className="me-1 " + badgeClass(category, subset))

def toBadge(dataset, category, subset):
    return '<span class="badge rounded-pill '+badgeClass(category, subset)+'">'+translateCategory(dataset, category, subset) +'</span>'

def getBadges(category, dataset, subsets):
    # Read the descriptors:
    badges = [toBadge(dataset, category, x) for x in subsets]
    
    if category+'.*' in SUBSET_TYPES:
        badges = [toBadge(dataset, category, '*')] + badges
    
    return ' '.join([x for x in badges])

#@app.callback(
#    Output("download-ds", "data"),
##     Output({'type': 'download-ds-file', 'index': MATCH}, 'n_clicks'),
#    Input({'type': 'download-ds-file', 'index': ALL}, 'n_clicks'),
#    State({'type': 'download-ds-file', 'index': ALL}, 'id'),
#    prevent_initial_call=True,
#)
#def download(n_clicks, id):
#    triggered = [t["prop_id"] for t in dash.callback_context.triggered][0]
#    triggered = eval(triggered.replace('.n_clicks', ''))
#    href = triggered['index']
#    href = glob.glob(os.path.join(DATA_PATH, '*', href))[0]
#    return dcc.send_file(href)