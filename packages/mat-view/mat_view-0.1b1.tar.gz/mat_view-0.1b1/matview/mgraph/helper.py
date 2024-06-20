# Helpers for tree structures
# -----------------------------------------------------------------------
def convert2anytree(tree, parent=None, parentNode=None): 
    from anytree import Node, RenderTree
    from anytree.exporter import DotExporter
    
    if parent is None:
        root = Node(tree)
    else:
        root = Node(tree, parent=parentNode)
                
    for child in tree.children:
        convert2anytree(child, tree, root)
        
    return root

def resder_anytree(tree):
    from anytree import RenderTree
    root_node = convert2anytree(tree)
    root_node = RenderTree(root_node)
    return root_node

def convert2digraph(tree, dot=None):
    from graphviz import Digraph
    
    if dot is None:
        dot = Digraph(comment='Tree')
        dot.node(str(tree.data.mid), tree.data.toText())
    
    for node in tree.children:
        dot.node(str(node.data.mid), node.data.toText() + ' - ' + '{:3.2f}'.format(node.parentSim))
        dot.edge(str(tree.data.mid), str(node.data.mid))
        convert2digraph(node, dot)
        
    return dot

# ------------------------------------------------------------------------------------------------------------
def get_pointfeature(p, attribute=None):
    if attribute is None:
#        return '\\n'.join([format_attr(k, v) for k,v in p.items()])
        return ','.join( list(map(lambda i: format_attr(i, p.aspects[i]), range(len(p.aspects)))) )
    else:
        return str(p.aspects[attribute])
    
def format_attr(key, val, masks={}):
#    return str(str(key)+' '+str(val))
    return str(val)
# -----------------------------------------------------------------------