import pandas as pd

def trajectory_stats(ls_trajs):
    samples = len(ls_trajs)
    labels = set()
    top = 0
    bot = float('inf')
    npoints = 0
    classes = {}
    
    def processT(T):
        nonlocal npoints, top, bot, labels, classes
        labels.add(T.label)
        classes[T.label] = 1 if T.label not in classes.keys() else classes[T.label]+1
        npoints += T.size
        top = max(top, T.size)
        bot = min(bot, T.size)
    
    list(map(lambda T: processT(T), ls_trajs))
    
    labels = [str(l) for l in labels]
    labels.sort()
    avg_size = npoints / samples
    diff_size = max( avg_size - bot , top - avg_size)
#    attr = list(map(lambda attr: attr.text, ls_trajs[0].attributes)) #list(ls_trajs[0].points[0].keys())
    attr = ls_trajs[0].attribute_names
    num_attr = len(attr)
    
    return labels, samples, top, bot, npoints, avg_size, diff_size, attr, num_attr, classes

def movelet_stats(movelets):
    df_stats = pd.DataFrame()

    l = len(movelets)
    def processMov(m):
        points = m.points

        stats = {
            'movelet_id': m.mid,
            'tid': m.tid,
            'label': m.trajectory.label,
            'size': m.size,
            'quality': m.quality.value,
            'n_features': m.l,
        }
        
#        stats.update({k: 1 for k in list(points[0].keys())})
        stats.update(dict(map(lambda k: (k, 1), m.attribute_names)))
    
        return stats#df_stats.append(stats, ignore_index=True)

    df_stats = pd.DataFrame.from_records( list(map(lambda m: processMov(m), movelets)) )
    
    cols = ['movelet_id', 'tid', 'label', 'size', 'quality', 'n_features']
    cols = cols + [x for x in df_stats.columns if x not in cols]
    return df_stats[cols]

def movelet_stats_bylabel(df, label='label'):
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
        
#        stats.update({k: aux_df[k].sum() for k in feat_cols})
        stats.update(dict(map(lambda k: (k, aux_df[k].sum()), feat_cols)))
        
        return stats
        
    df_stats = pd.DataFrame.from_records( list(map(lambda lbl: processLabel(lbl), df[label].unique())) )

    cols = ['label', 'movelets', 'mean_quality', 'min_quality', 'max_quality', 
            'mean_size', 'min_size', 'max_size',
            'mean_n_features', 'min_n_features', 'max_n_features']
    
    cols = cols + [x for x in df_stats.columns if x not in cols]
    
    df_stats = df_stats.fillna('-')
    
    return df_stats[cols]