# Heat Map
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('agg')

from matview.util.stats import movelet_stats, movelet_stats_bylabel
    
def render(movelets, attribute=None, title='Attribute per Class Label HeatMap'):
    df = movelet_stats_bylabel(movelet_stats(movelets))
    
    # Create a dataset
    dfheat = df.set_index('label')
    dfheat = dfheat.replace(['-'],0)
    dfheat[df.iloc[:,11:].columns] = dfheat[df.iloc[:,11:].columns].astype(float)
    dfheat[df.iloc[:,11:].columns] = dfheat[df.iloc[:,11:].columns].div(dfheat['movelets'], axis=0)
    # Default heatmap
    plt.figure(figsize=(20,5)) # 'lat_lon'
    p1 = sns.heatmap(dfheat[df.iloc[:,11:].columns].T, cmap="Spectral_r") #'lat_lon'
    p1.set(xlabel='Class Label', ylabel='Attribute', title=title)
    plt.tight_layout()
    
    return p1.get_figure()

# ------------------------------------------------------------------------------------------------------------
'''
def movelets_statistics(movelets):    
    df_stats = pd.DataFrame()

    l = len(movelets)
    def processMov(m):

        points = m.points

        stats = {
            'movelet_id': m.mid,
            'tid': m.trajectory.tid,
            'label': m.trajectory.label,
            'size': m.size,
            'quality': m.quality.value,
            'n_features': m.l,
#             'features': ', '.join(list(points[0].keys())),
        }
        
        stats.update({k: 1 for k in list(points[0].keys())})
    
        return stats

    df_stats = pd.DataFrame.from_records( list(map(lambda m: processMov(m), movelets)) )
    
    cols = ['movelet_id', 'tid', 'label', 'size', 'quality', 'n_features']#, 'features']
    cols = cols + [x for x in df_stats.columns if x not in cols]
    return df_stats[cols]

def movelets_statistics_bylabel(df, label='label'):
    df_stats = pd.DataFrame()
    
    def countFeatures(used_features, f):
        for s in f.split(', '):
            used_features[s] = used_features[s]+1 if s in used_features.keys() else 1

    cols = ['movelet_id', 'tid', 'label', 'size', 'quality', 'n_features']
    feat_cols = [x for x in df.columns if x not in cols]
            
    def processLabel(lbl):
        aux_df = df[df['label'] == lbl]
        stats = aux_df.describe()

        stats = {
            'label': lbl,
            'movelets': len(aux_df['movelet_id'].unique()),
            'mean_size': stats['size']['mean'],
            'min_size': stats['size']['min'],
            'max_size': stats['size']['max'],
            'mean_quality': stats['quality']['mean'],
            'min_quality': stats['quality']['min'],
            'max_quality': stats['quality']['max'],
            'mean_n_features': stats['n_features']['mean'],
            'min_n_features': stats['n_features']['min'],
            'max_n_features': stats['n_features']['max'],
        }
        
        stats.update({k: aux_df[k].sum() for k in feat_cols})

        return stats
        
    df_stats = pd.DataFrame.from_records( list(map(lambda lbl: processLabel(lbl), df[label].unique())) )
    
    cols = ['label', 'movelets', 'mean_quality', 'min_quality', 'max_quality', 
            'mean_size', 'min_size', 'max_size',
            'mean_n_features', 'min_n_features', 'max_n_features']
    cols = cols + [x for x in df_stats.columns if x not in cols]
    
    df = df_stats[cols]
    return df.fillna('-')
'''