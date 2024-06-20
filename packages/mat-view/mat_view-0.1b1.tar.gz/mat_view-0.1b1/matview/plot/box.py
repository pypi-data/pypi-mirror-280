# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

matplotlib.use('agg')
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Arial'

from matview.util.format import *
from matview.web.definitions import *

def render(df, column=None, methods_order=None, datasets_order=None, models_order=None, plot_type='box'):
    metric = metricName(column)
    pc = PlotConfig()
    
    if column.replace('metric:', '') in ['accuracy', 'accuracyTop5']:
#        pc.lim = (-5, 105)
#        pc.suffix = '%'
        pc.lim = (-5, 1.05)
        pc.suffix = ''
        metric += ' (' + ','.join(set(df['model'].unique()) - set('-')) + ')'
        return boxPlot(df, column, title=metric, methods_order=methods_order, plot_config=pc, plot_type=plot_type)
    elif column.replace('metric:', '') in ['f1_score', 'precision', 'recall', 'loss']:
        pc.lim = (-0.05, 1.05)
        return boxPlot(df, column, title=metric, methods_order=methods_order, plot_config=pc, plot_type=plot_type)
    elif column.replace('metric:', '') in ['clstime', 'runtime', 'totaltime']:
        pc = HourConfig()
        pc.autoticks(df[column].max())
        return boxPlot(df, column, title=metric, methods_order=methods_order, plot_config=pc, plot_type=plot_type)
    elif column.replace('metric:', '') in ['candidates', 'movelets']:
        def format_metric(x):
            val = x/1000
            return '{:,.{}f}'.format(val, 0 if val > 1 else 1)
        pc.scale = 1000
        pc.suffix = 'k'
        pc.format_func = format_metric
        return boxPlot(df, column, title=metric, methods_order=methods_order, plot_config=pc, plot_type=plot_type)
    else:
        return boxPlot(df, column, title=metric, methods_order=methods_order, plot_config=pc, plot_type=plot_type)
    
# -----------------------------------------------------------------------
def boxPlot(df, column, title='', methods_order=None, plot_config=PlotConfig(), plot_type='box'): # Box or Swarm
    
    n = len(df)
    df.drop(df[df['error'] == True].index, inplace=True)
    print('[WARN Box Plot:] Removed results due to run errors:', n - len(df))

    if not methods_order:
        methods_order = list(df['method'].unique())

    df['methodi'] = df['method'].apply(lambda x: {methods_order[i]:i for i in range(len(methods_order))}[x])
    df = df.sort_values(['methodi', 'dataset', 'subset'])

#    df['method'] = list(map(lambda m: METHOD_NAMES[m] if m in METHOD_NAMES.keys() else m, df['method']))
    
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

    df['key'] = df['dataset']+'-'+df['subset']
    if len(set(df['model'].unique()) - set('-')) > 1:
        df['name'] = df['method'] + list(map(lambda x: '-'+x if x != '-' else '', df['model']))
    else:
        df['name'] = df['method']

    sns.set(font_scale=1.5)
    sns.set_style("ticks")
    
    def boxplot(df, col, xl):    
        plt.figure(figsize=(plot_config.plotsize[0],0.3*len(df['name'].unique())+1)) 
        if plot_type == 'swarm':
            p1 = sns.swarmplot(data=df[['key', 'name', col]], y="name", x=col, palette=mypal)
        else: # Default: boxplot
            p1 = sns.boxplot(data=df[['key', 'name', col]], y="name", x=col, palette=mypal)
        
        #plt.xticks(rotation=80)
        p1.set(xlabel=xl, ylabel='Method', title='')
        
        # the y labels
        if plot_config.ticks:
            p1.set_xticks(plot_config.ticks)
            xlabels = list(map(lambda x: plot_config.format_axis(x), plot_config.ticks))
            p1.set_xticklabels(xlabels)
        else:
            if plot_config.lim:
                p1.set(xlim = plot_config.lim)
            else: #elif not mean_aggregation:
                xmax = df[column].max()
                xmax = xmax * 1.2
                p1.set(xlim = (0, xmax))
            ticks_loc = p1.get_xticks().tolist()
            xlabels = list(map(lambda x: plot_config.format_axis(x), p1.get_xticks().tolist()))
            p1.set_xticklabels(xlabels)
            
        plt.grid()
        plt.tight_layout()
        return p1.get_figure()
    
    return boxplot(df, column, xl=title)