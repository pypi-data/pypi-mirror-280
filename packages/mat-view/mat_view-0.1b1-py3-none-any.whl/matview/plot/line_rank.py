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

def render(df, column=None, methods_order=None, datasets_order=None, models_order=None):
    metric = metricName(column)
    pc = PlotConfig()
    
    if column.replace('metric:', '') in ['accuracy', 'accuracyTop5']:
#        pc.lim = (-5, 105)
#        pc.suffix = '%'
        pc.lim = (-5, 1.05)
        pc.suffix = ''
        metric += ' (' + ','.join(set(df['model'].unique()) - set('-')) + ')'
        return lineRank(df, column, title=metric, methods_order=methods_order, plot_config=pc)
    elif column.replace('metric:', '') in ['f1_score', 'precision', 'recall', 'loss']:
        pc.lim = (-0.05, 1.05)
        return lineRank(df, column, title=metric, methods_order=methods_order, plot_config=pc)
    elif column.replace('metric:', '') in ['clstime', 'runtime', 'totaltime']:
        pc = HourConfig()
        pc.autoticks(df[column].max())
        return lineRank(df, column, title=metric, methods_order=methods_order, plot_config=pc)
    elif column.replace('metric:', '') in ['candidates', 'movelets']:
        def format_metric(x):
            val = x/1000
            return '{:,.{}f}'.format(val, 0 if val > 1 else 1)
        pc.scale = 1000
        pc.suffix = 'k'
        pc.format_func = format_metric
        return lineRank(df, column, title=metric, methods_order=methods_order, plot_config=pc)
    else:
        return lineRank(df, column, title=metric, methods_order=methods_order, plot_config=pc)
    
# -----------------------------------------------------------------------
def lineRank(df, column, title='', methods_order=None, datasets_order=None, plot_config=PlotConfig()): # plot_type='box' | 'swarm'
    n = len(df)
    df.drop(df[df['error'] == True].index, inplace=True)
    print('[WARN Line Rank Plot:] Removed results due to run errors:', n - len(df))

    if not methods_order:
        methods_order = list(df['method'].unique())
    
    df['key'] = list(map(lambda d,s: datasetName(d,s), df['dataset'], df['subset']))
    df = df.groupby(['key', 'name', 'dataset', 'subset', 'method', 'model'])[column].mean().reset_index()

    df['methodi'] = df['method'].apply(lambda x: {methods_order[i]:i for i in range(len(methods_order))}[x])
    df = df.sort_values(['methodi', 'dataset', 'subset'])

    df['method'] = list(map(lambda m: METHOD_NAMES[m] if m in METHOD_NAMES.keys() else m, df['method']))

    # ---
    # COLOR PALETTE:
    mypal = list(df['key'].unique())
    mypal.sort()
    pale = 'husl' #"Spectral_r"
    colors = sns.color_palette(pale, len(mypal))
    mypal = {mypal[i]:colors[i] for i in range(len(mypal))}
    # ---
    
    if len(set(df['model'].unique()) - set('-')) > 1:
        df['name'] = df['method'] + list(map(lambda x: '-'+x if x != '-' else '', df['model']))
    else:
        df['name'] = df['method']
    
    sns.set(font_scale=1.5)
    sns.set_style("ticks")
    
#    plt.figure(figsize=(0.5*len(df['name'].unique())+1,0.5*len(df['key'].unique())+1)) 
    plt.figure(figsize=plot_config.plotsize)

#    for datakey in ds_wide['key'].unique()
    p1 = sns.lineplot(data=df[['key', 'name', column]], x='name', y=column, hue='key', palette=mypal)

    p1.set(ylabel=title, xlabel='Method', title='')
    plt.xticks(rotation=80)
    p1.legend(loc='upper left', bbox_to_anchor=(1, 0.5))

#    if xaxis_format:
#        if xaxis_format[0]:
#            p1.set(ylim = xaxis_format[0])
#        ticks_loc = p1.get_yticks().tolist()
#        xlabels = ['{:,.1f}'.format(x/xaxis_format[1]) + xaxis_format[2] for x in ticks_loc]
#        #p1.set_xticks(ticks_loc)
#        p1.set_yticklabels(xlabels)
        
    # the y labels
    if plot_config.ticks:
        p1.set_yticks(plot_config.ticks)
        xlabels = list(map(lambda x: plot_config.format_axis(x), plot_config.ticks))
        p1.set_yticklabels(xlabels)
    else:
        if plot_config.lim:
            p1.set(ylim = plot_config.lim)
        else:
            ymax = df[column].max()
            ymax = ymax * 1.2
            p1.set(ylim = (0, ymax))
        ticks_loc = p1.get_yticks().tolist()
        xlabels = list(map(lambda x: plot_config.format_axis(x), p1.get_yticks().tolist()))
        p1.set_yticklabels(xlabels)

    plt.grid()
    plt.tight_layout()
    return p1.get_figure()