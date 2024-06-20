#     import networkx as nx
#     import pandas as pd
#     import matplotlib as mat
from graphviz import Digraph
# -----------------------------------------------------------------------
def render(movelets, attribute=None, title='Movelets Markov Tree', concat_edges=True):    
    G = Digraph(comment=title)
#     G.attr(fontsize='10')
    nodes = set()
    edges = dict()
    for mov in movelets:
        p1 = mov.data[0]
        if attribute == None or attribute in p1.keys():
            with G.subgraph(name='cluster_'+str(mov.mid)) as dot:
                dot.attr(color='blue')
                dot.attr(label='#'+str(mov.mid)+' ({:3.2f}%)'.format(mov.quality))
                if get_pointfeature(p1,attribute) not in nodes:
                    nodes.add(get_pointfeature(p1,attribute))
                    dot.node(get_pointfeature(p1,attribute), get_pointfeature(p1,attribute))#, fontsize='10')
#                     dot.attr(fontsize='10')

                if len(mov.data) > 1:
                    for i in range(1, len(mov.data)):
                        p = mov.data[i]
                        if get_pointfeature(p,attribute) not in nodes:
                            nodes.add(get_pointfeature(p,attribute))
                            dot.node(get_pointfeature(p,attribute), get_pointfeature(p,attribute))#, fontsize='10')
                        # EDGE:
                        ed = get_pointfeature(p1,attribute)+','+get_pointfeature(p,attribute)
                        edlbl = ' #'+str(mov.mid)+'.'+str(i)
                        if concat_edges and ed in edges.keys():
                            edges.update({ed: edges[ed] +', '+ edlbl})
                        else:
                            edges.update({ed: edlbl})
                        
                        p1 = p
        else: 
            continue
        
    for key, value in edges.items():
        key = key.split(',')
        G.edge(key[0], key[1], value, fontsize='10')
    return G