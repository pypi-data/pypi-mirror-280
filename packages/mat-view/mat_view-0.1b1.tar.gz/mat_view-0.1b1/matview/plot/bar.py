# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

matplotlib.use('agg')
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Arial'

from matview.util.format import PlotConfig, HourConfig, format_hour
from matview.web.definitions import *

def render(df, column=None, methods_order=None, datasets_order=None, models_order=None, aggregate_ds=False):
    metric = metricName(column) 
#    pc = PlotConfig(label_pos = [-15,0] if aggregate_ds else [0,0])
    pc = PlotConfig(label_pos = [0,0])
    
    if column.replace('metric:', '') in ['accuracy', 'accuracyTop5'] or df[column].max() <= 1.0:
#        pc.lim = (0, 105)
#        pc.suffix = '%'
        pc.lim = (0, 1.05)
        pc.suffix = ''
#        pc.label_pos[1] = -15
        pc.mask = '{:,.2f}' #'{:,.1f}'
#        fmt = {'ylim': (0, 105), 'scale':1, 'suffix':'%', 'label_pos':(label_pos[0],-15), 'mask':'{:,.1f}'}
        metric += ' (' + ','.join(set(df['model'].unique()) - set('-')) + ')'
        return barPlot(df, column, title=metric, methods_order=methods_order, datasets_order=datasets_order, 
                              plot_config=pc, mean_aggregation=aggregate_ds)
#    elif column.replace('metric:', '') in ['f1_score', 'precision', 'recall', 'loss']:
#        pc.lim = (0, 1.05)
#        pc.scale = 1.0
#        pc.label_pos[1] = -15
#        pc.mask = '{:,.2f}'
#        return barPlot(df, column, title=metric, methods_order=methods_order, datasets_order=datasets_order, 
#                              plot_config=pc, mean_aggregation=aggregate_ds)
#        fmt = {'ylim': (0, 1.05), 'scale':1.0, 'suffix':'', 'label_pos':(label_pos[0],-15), 'mask':'{:,.2f}'}
#    else:
#        pc.scale = 1.0
#        pc.label_pos[1] = -15
#        pc.mask = '{:,.2f}'
#        fmt = {'scale':1.0, 'suffix':'', 'label_pos':label_pos}
    
    elif column.replace('metric:', '') in ['clstime', 'runtime', 'totaltime'] or 'time' in column.replace('metric:', ''):
#        def format_metric(x):
#            s = format_hour(x)
#            return s[:s.find('m')] if 'h' in s else (s[:s.find('m')+1] if 'm' in s else s) #s[:s.find('m')+1]
        
#        pc.scale = 3600000 # 1h in milliseconds
#        pc.format_func = format_metric
#        fmt = {'scale':3600000, 'suffix':'', 'format_func':format_metric, 'label_pos':label_pos}
        pc = HourConfig(label_pos=pc.label_pos)
        pc.autoticks(df[column].max())
        return barPlot(df, column, title=metric, methods_order=methods_order, datasets_order=datasets_order, 
                              plot_config=pc, mean_aggregation=aggregate_ds)#, plot_type=plot_type)
    elif column.replace('metric:', '') in ['candidates', 'movelets']:
        def format_metric(x):
            val = x/1000
            return '{:,.{}f}'.format(val, 0 if val > 1 else 1)
        pc.scale = 1000
        pc.suffix = 'k'
        pc.format_func = format_metric
#        fmt = {'scale':1000, 'suffix':'k', 'format_func':format_metric, 'label_pos':label_pos}
        return barPlot(df, column, title=metric, methods_order=methods_order, datasets_order=datasets_order, 
                              plot_config=pc, mean_aggregation=aggregate_ds)#, plot_type=plot_type)
    else:
        return barPlot(df, column, title=metric, methods_order=methods_order, datasets_order=datasets_order, 
                              plot_config=pc, mean_aggregation=aggregate_ds)
    

# -----------------------------------------------------------------------
def barPlot(df, column, title='', methods_order=None, datasets_order=None, plot_type='bar', mean_aggregation=False, 
            plot_config=PlotConfig()): # plot_type='bar' | 'line'
    n = len(df)
    df.drop(df[df['error'] == True].index, inplace=True)
    print('[WARN Bar Plot:] Removed results due to run errors:', n - len(df))

    if not methods_order:
        methods_order = list(df['method'].unique())
        
    if not datasets_order:
        datasets_order = list(df['dataset'].unique())
        datasets_order.sort()

    df = df.groupby(['name', 'method', 'model', 'dataset', 'subset'])[column].mean().reset_index()
    
    df['key'] = list(map(lambda d,s: datasetName(d,s), df['dataset'], df['subset']))

    df['methodi'] = df['method'].apply(lambda x: {methods_order[i]:i for i in range(len(methods_order))}[x])
    df['dsi'] = df['key'].apply(lambda x: {datasets_order[i]:i for i in range(len(datasets_order))}[x])
    df = df.sort_values(['methodi', 'dsi'])

#    df['method'] = list(map(lambda m: METHOD_ABRV[m] if m in METHOD_ABRV.keys() else m, df['method']))
    
    # ---
    # COLOR PALETTE:
    pre = 6
    mypal = df['method'].unique()
    mypal_idx = list(set([x[:pre] for x in mypal]))
    mypal_idx.sort()
    pale = 'husl' #"Spectral_r"
    colors = sns.color_palette(pale, len(mypal_idx))
    mypal_idx = {mypal_idx[i]:colors[i] for i in range(len(mypal_idx))}
    mypal_idx = {x: mypal_idx[x[:pre]] for x in mypal}
    from itertools import product
    clas = df['model'].unique()
    mypal = {k+'-'+x:v for x in clas for k,v in mypal_idx.items()}
    mypal.update(mypal_idx)
    # ---
    
    if len(set(df['model'].unique()) - set('-')) > 1:
        df['name'] = df['method'] + list(map(lambda x: '-'+x if x != '-' else '', df['model']))
    else:
        df['name'] = df['method']
    
    sns.set(font_scale=1.5)
    sns.set_style("ticks")
    
    a_size = 0.03*len(df['key'].unique())+1
    b_size = 100
    
    a_size = 0.03*len(df['key'].unique())+1
    plt.figure(figsize=plot_config.plotsize) 
    plt.rcParams['font.size'] = 12

    if mean_aggregation:
        p1 = sns.barplot(df[['key', 'name', column]], x='name', y=column, palette='husl')#mypal)
    else:
        p1 = sns.barplot(df[['key', 'name', column]], x='name', y=column, hue='key', palette='husl')#mypal)
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=100, borderaxespad=0.)

    p1.set(ylabel=title, xlabel='Method', title='')
    plt.xticks(rotation=plot_config.xrotation, horizontalalignment='right')

    
#    if plot_config.ylim:
#        p1.set(ylim = plot_config.ylim)
#    else: #elif not mean_aggregation:
#        ymax = df[column].max()
#        ymax = ymax * 1.2
#        p1.set(ylim = (0, ymax))
#    ticks_loc = p1.get_yticks().tolist()
#    xlabels = [plot_config.format_axis(x) for x in ticks_loc]
#    p1.set_yticklabels(xlabels)

    # the y labels
    if plot_config.ticks:
        p1.set_yticks(plot_config.ticks)
        xlabels = list(map(lambda x: plot_config.format_axis(x), plot_config.ticks))
        p1.set_yticklabels(xlabels)
    else:
        if plot_config.lim:
            p1.set(ylim = plot_config.lim)
        else: #elif not mean_aggregation:
            ymax = df[column].max()
            ymax = ymax * 1.2
            p1.set(ylim = (0, ymax))
        ticks_loc = p1.get_yticks().tolist()
        xlabels = list(map(lambda x: plot_config.format_axis(x), p1.get_yticks().tolist()))
#        [plot_config.format_axis(x) for x in ticks_loc]
        p1.set_yticklabels(xlabels)

    for container in p1.containers:
        p1.bar_label(container, labels=list(map(lambda x: plot_config.format_val(x), container.datavalues)), 
                     rotation=plot_config.label_rotation, horizontalalignment='center', position=plot_config.label_pos)

    plt.tight_layout()
    return p1.get_figure()

# DEPRECATED - TODO Needs Updating -----------------------------------------------------------------------
def hbarPlot(df, column, title='', methods_order=None, xaxis_format=False, plot_type='bar'): # plot_type='bar' | 'line'
    n = len(df)
    df.drop(df[df['error'] == True].index, inplace=True)
    print('[WARN H. Bar Plot:] Removed results due to run errors:', n - len(df))

    if not methods_order:
        methods_order = list(df['method'].unique())
        
    df = df.groupby(['name', 'method', 'model', 'dataset', 'subset'])[column].mean().reset_index()

    df['methodi'] = df['method'].apply(lambda x: {methods_order[i]:i for i in range(len(methods_order))}[x])
    df = df.sort_values(['methodi', 'dataset', 'subset'])

    df['method'] = list(map(lambda m: METHOD_NAMES[m] if m in METHOD_NAMES.keys() else m, df['method']))
    
    df['key'] = list(map(lambda d,s: datasetName(d,s), df['dataset'], df['subset']))

    # ---
    # COLOR PALETTE:
    pre = 6
    mypal = df['method'].unique()
    mypal_idx = list(set([x[:pre] for x in mypal]))
    mypal_idx.sort()
    pale = 'husl' #"Spectral_r"
    colors = sns.color_palette(pale, len(mypal_idx))
    mypal_idx = {mypal_idx[i]:colors[i] for i in range(len(mypal_idx))}
    mypal_idx = {x: mypal_idx[x[:pre]] for x in mypal}
    from itertools import product
    clas = df['model'].unique()
    mypal = {k+'-'+x:v for x in clas for k,v in mypal_idx.items()}
    mypal.update(mypal_idx)
    # ---
    
    if len(set(df['model'].unique()) - set('-')) > 1:
        df['name'] = df['method'] + list(map(lambda x: '-'+x if x != '-' else '', df['model']))
    else:
        df['name'] = df['method']
    
    sns.set(font_scale=1.5)
    sns.set_style("ticks")
    
    a_size = 0.03*len(df['key'].unique())+1
    b_size = 100
    
    a_size = 0.03*len(df['key'].unique())+1
    plt.figure(figsize=(15,5)) 
        
    p1 = sns.barplot(df[['key', 'name', column]], y='key', x=column, hue='name', palette='husl')#mypal)

    p1.set(xlabel=title, ylabel='Dataset', title='')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., title='Method')

    if xaxis_format:
        if xaxis_format[0]:
            p1.set(xlim = xaxis_format[0])
        ticks_loc = p1.get_xticks().tolist()
        xlabels = ['{:,.1f}'.format(x/xaxis_format[1]) + xaxis_format[2] for x in ticks_loc]
        p1.set_xticklabels(xlabels)

    plt.grid()
    plt.tight_layout()
    return p1.get_figure()