import pandas as pd
import matplotlib.pyplot as plt
import plotly
from plotly import graph_objects as go

from matview.view.helper import get_pointfeature

# -----------------------------------------------------------------------
def render(movelets, attribute=None, title='Movelets Sankey Diagram'):
    # Source: https://gist.github.com/praful-dodda/c98d9fd5dab6e6a9e68bf96ee73630e9
    # maximum of 6 value cols -> 6 colors
    colorPalette = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896',
                    '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7',
                    '#bcbd22', '#dbdb8d','#17becf', '#9edae5']
    colorNumList = []
    specials = [". ","> ",">> ",".. ","- "]
    
    labels = set()
    labelDict = {}
    lvlDict = {}
    cat_cols = []
    
    def lbladd(x, i):
        x_str = x + ' |'+str(i)#+']'
        if x_str not in labels:
            labels.add(x_str)
            labelDict[x_str] = len(labelDict)
        lvladd(i, labelDict[x_str], x_str)
        return (labelDict[x_str], x_str)

    def lvladd(lvl, idx, x):
        l = 'lv'+str(lvl)
        if l not in cat_cols:
            cat_cols.append(l)
        if l not in lvlDict.keys():
            lvlDict[l] = dict()
        lvlDict[l][idx] = x
        
    sourceTargetDf = pd.DataFrame()
    
    aux_mov = []
#    for m in movelets:
    def select(m):
        if attribute and attribute not in m.attribute_names:
#            continue
            return False
        idx, x = lbladd(m.trajectory.label, 1)
#        aux_mov.append(m)
        return True
    aux_mov = list(filter(lambda m: select(m), movelets))
    
#     aux_mov = movelets.copy()
    
    has_lvl = True
    i = 0
    while has_lvl:
        has_lvl = False
#        for m in aux_mov:
        def process(m):
            nonlocal sourceTargetDf, aux_mov, has_lvl
        
            if i < len(m.points):
                
                if attribute == None:
                    attr_idx = None 
                elif attribute in m.attribute_names:
                    attr_idx = m.attribute_names.index(attribute)
#                else:
#                    return
                
                has_lvl = True
            
                if i == 0:
                    last_idx, last_x = lbladd(m.trajectory.label, 1)
                else:
                    last_idx, last_x = lbladd(get_pointfeature(m.points[i-1], attr_idx), i+1)

                idx, x = lbladd(get_pointfeature(m.points[i], attr_idx), i+2)

                aux_df = {}
                aux_df['source'] = last_x
                aux_df['target'] = x
                aux_df['s'] = 'lv'+str(i+1)
                aux_df['t'] = 'lv'+str(i+2)
                aux_df['label'] = m.trajectory.label
                aux_df['value'] = 1
                
                sourceTargetDf = sourceTargetDf.append(aux_df, ignore_index=True)
            else:
                aux_mov.remove(m)
        
        list(map(lambda m: process(m), aux_mov))
        i += 1
        
    sourceTargetDf = sourceTargetDf.groupby(['source','target','s','t','label']).agg({'value':'sum'}).reset_index()
    sourceTargetDf = sourceTargetDf.sort_values(by=['s', 't', 'label', 'source','target'])

    # List of labels:
#    labelList = list((v, k) for k, v in labelDict.items())
    labelList = list(map(lambda kv: (kv[1], kv[0]), labelDict.items()))
    
    # revese the dict 
#    rDict = {}
#    for k,v in lvlDict.items():
#        rDict[k] = {str(v) : k for k,v in v.items()}
        
    rDict = dict(map(lambda lkv: 
                     (lkv[0], dict(map(lambda rkv: (str(rkv[1]), rkv[0]), lkv[1].items()))),  
            lvlDict.items()))
        
#    rDict = dict(map(lambda lkv: 
#                     ( lkv[0], dict(map(lambda kv: (str(kv[0]), kv[1]), lkv[1].items())) ), 
#                lvlDict.items() ))
    
    # define colors based on number of levels
    colorList = []
    for idx, colorNum in enumerate(colorNumList):
        colorList = colorList + [colorPalette[idx]]*colorNum
        
    # transform df into a source-target pair
    reset_level = 0
    
    ### Combining codes for placing elements at their corresponding vertical axis.
    unique_list = []
    def combine(k, v):
        nonlocal reset_level
#    for k,v in rDict.items():
#        v_keys = [x+'_'+str(reset_level) for x in list(v.keys())]
        v_keys = list(map(lambda x: x+'_'+str(reset_level), list(v.keys()) ))
        reset_level += 1
        if v_keys[0][:3] == 'nan':
            v_keys.pop(0)
#        [unique_list.append(x) for x in v_keys]
        list(map(lambda x: unique_list.append(x), v_keys))
    list(map(lambda kv: combine(*kv), rDict.items()))
    
    nodified = nodify_sankey(unique_list)
    
    sourceTargetDf = sourceTargetDf[(sourceTargetDf['source']!='nan') & (sourceTargetDf['target']!='nan')]
    sourceTargetDf['sourceID'] = sourceTargetDf.apply(lambda x: rDict[x['s']][x['source']], axis=1)
    sourceTargetDf['targetID'] = sourceTargetDf.apply(lambda x: rDict[x['t']][x['target']], axis=1)
    
#     return sourceTargetDf
    
    # creating the sankey diagram
    data = dict(
        type='sankey',
        arrangement = "snap",
        orientation = 'h',
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(
            color = "black",
            width = 0.5
          ),
          label = [x[1] for x in labelList],
#           color = colorList,
          x=nodified[0],
          y=nodified[1]
        ),
        link = dict(
          source = sourceTargetDf['sourceID'],
          target = sourceTargetDf['targetID'],
          value = sourceTargetDf['value'],
          label = sourceTargetDf['label'],
#           color = colorList
        )
      )
    
    layout =  dict(
        title = title,
        height = 1000,
#        width = 950,
        font = dict(
          size = 12
        )
    )
       
    fig = go.Figure(data = [go.Sankey(data)], layout=layout)
    return fig

def nodify_sankey(node_names):
    ends = sorted(list(set([e[-1] for e in node_names])))
    
    # intervals
    steps = 1.3/len(ends)

    # x-values for each unique name ending
    # for input as node position
    nodes_x = {}
    xVal = 0
    for e in ends:
        nodes_x[str(e)] = xVal
        xVal += steps

    # x and y values in list form
    x_values = [nodes_x[n[-1]] for n in node_names]
    y_values = [.1]*len(x_values)
    
    return x_values, y_values
