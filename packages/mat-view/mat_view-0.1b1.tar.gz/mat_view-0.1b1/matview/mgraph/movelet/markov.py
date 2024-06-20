import networkx as nx
#     import pandas as pd
import matplotlib as mat
from graphviz import Digraph

from matview.view.helper import get_pointfeature
# -----------------------------------------------------------------------
def render(movelets, attribute=None, title='Movelets Markov Graph', concat_edges=True):
    nodes, edges, groups, no_colors, ed_colors = movelets_markov(movelets, attribute, concat_edges=concat_edges)
    
    # Create Graph
    return graph_nx(title, nodes, edges, groups, no_colors, ed_colors, draw=False)
    
def movelets_markov(movelets, attribute=None, concat_edges=True):
    SEP = '|'
    
    nodes = []
    groups = []
    edges = dict()
    no_colors = dict()
    ed_colors = dict()
#    for mov in movelets:
    def process(mov):
        p1 = mov.points[0]
        
        if attribute == None:
            attr_idx = None 
        elif attribute in mov.attribute_names:
            attr_idx = mov.attribute_names.index(attribute)
        else:
            return
        
#        if attribute == None or attribute in mov.attribute_names: #keys():
        gp = '#'+str(mov.mid)+' ({:3.2f}%)'.format(mov.quality.value)
        if gp not in groups:
            groups.append(gp)

        no1 = get_pointfeature(p1, attr_idx)
        if no1 not in nodes:
            nodes.append(no1)
            no_colors[no1] = gp

        if len(mov.points) > 1:
#            for i in range(1, len(mov.points)):
            def processPoint(i):
                nonlocal p1, attr_idx
                p2 = mov.points[i]
                no2 = get_pointfeature(p2, attr_idx)
                if no2 not in nodes:
                    nodes.append(no2)
                    no_colors[no2] = gp
                # EDGE:
                ed  = no1+SEP+no2
                edl = ' #'+str(mov.mid)+'.'+str(i)

                if ed not in ed_colors.keys():
                    ed_colors[ed] = gp

                if concat_edges and ed in edges.keys():
                    edges.update({ed: edges[ed] + 1})
                elif concat_edges:
                    edges.update({ed: 1})
                else:
                    edges.update({ed: edl})

                p1 = p2
            list(map(lambda i: processPoint(i), range(1, len(mov.points))))
                
    list(map(lambda mov: process(mov), movelets))

    return nodes, edges, groups, no_colors, ed_colors

# -----------------------------------------------------------------------        
def graph_nx(title, nodes, edges, groups, no_colors, ed_colors, draw=True):    
    SEP = '|'
    G = nx.DiGraph(name=title)
    G.add_nodes_from(nodes)
    
    edges_aux = [tuple(k.split(SEP)+[{'weight': v}]) for k,v in edges.items()]
    G.add_edges_from(edges_aux)

    cmap = mat.colors.ListedColormap(['C0', 'darkorange'])
    
    # Draw graph
    if draw:
        # Specify layout and colors
        ccod = pd.Categorical(groups).codes
        ecod = pd.Categorical([ccod[groups.index(ed_colors[x])] for x in edges.keys()]).codes
        ncod = pd.Categorical([ccod[groups.index(no_colors[x])] for x in nodes]).codes

        paux = max(edges.values())
        edge_sizes = [(x/paux)+1 for x in edges.values()]
        
        return nx.draw(G, with_labels=True, node_size=10000, node_color=ncod, cmap=cmap, width=edge_sizes, edge_color=ecod)
    else:
        
        # 2 ) get node pos
        pos = nx.circular_layout(G)
        # 3.) get cytoscape layout
        cy = nx.readwrite.json_graph.cytoscape_data(G)
#         return cy
        # 4.) Add the dictionary key label to the nodes list of cy
        for n in cy['elements']['nodes']:
            for k,v in n.items():
                v['label'] = v.pop('value')
        # 5.) Add the pos you got from (2) as a value for data in the nodes portion of cy
        scale = 150
        
        ecod = [mat.colors.rgb2hex(cmap(groups.index(ed_colors[x]))) for x in edges.keys()]
        ncod = [mat.colors.rgb2hex(cmap(groups.index(no_colors[x]))) for x in nodes]
        
        for n,p in zip(cy['elements']['nodes'],pos.values()):
            n['data']['color'] = str(ncod[nodes.index(n['data']['id'])])
        
        for n in cy['elements']['edges']:
            n['data']['color'] = str(ecod[list(edges.keys()).index(n['data']['source']+SEP+n['data']['target'])])
            
        elements_ls = cy['elements']['nodes'] + cy['elements']['edges']

        return elements_ls