# TODO Temporary added, maybe deprecated
# ------------------------------------------------------------------------------------------------------------
def render(movelets):
    raise Exception('Sub-module qstree: MoveletTree not implemented.')

class MoveletTree:
    def __init__(self, data, children=None):
        self.data      = data
        self.parentSim = 0
        
        self.children = []
        if children is not None:
            for child in self.children:
                self.add_child(child)
                
    def __repr__(self):
        return self.data.toString() + ' - ' + '{:3.2f}'.format(self.parentSim)
                
    def add(self, mov):
        assert isinstance(mov, Movelet)
        node = MoveletTree(mov)
        self.add_child(node)
        return node
                
    def add_child(self, node):
        assert isinstance(node, MoveletTree)
        self.children.append(node)
        
    def findSimilar(self, movelet, similarityFunction):
        sim  = similarityFunction(self.data, movelet)
        node = self
        for child in self.children:
            childSim, childNode = child.findSimilar(movelet, similarityFunction)
            if (childSim > sim):
                node = childNode
                sim  = childSim
        return sim, node
              
    def printNode(self, spacing='', parent=None):
        if parent is None:
            return (spacing + ' ' + self.data.toString()) + '\n'
        else:
            return (spacing + ' ' + self.data.diffPairs(parent.data)) + '\n'
        
    def traversePrint(self, spacing=''):
        s = self.printNode(spacing)
        for child in self.children:
            s += child.traversePrint(spacing + '-')
        return s

# ---------------------------
def similarity(mov1, mov2):
    total_size = mov1.size * len(mov1.data[0]) + mov2.size * len(mov2.data[0])
#     common_pairs = mov1.commonPairs(mov2)
#     return (len(common_pairs)*2 / total_size)
    common_pairs = mov1.commonPairs(mov2)
    common_size  = 0.0
        
    for m in [mov1, mov2]:
        for dictionary in m.data:
            for key in dictionary:
                if (key in dictionary and (key, dictionary[key]) in common_pairs):
                    common_size += 1.0
                    
#     print(common_pairs)
    return common_size / float(total_size)

# ---------------------------
def createTree(movelets):
    movelets.sort(key=lambda x: x.quality, reverse=True)
    
    tree = MoveletTree(movelets.pop(0))
    while len(movelets) > 0:
        mov = movelets.pop(0)
#         print(mov.toString())
        sim, node = tree.findSimilar(mov, similarity)
        node.add(mov).parentSim = sim
    return tree

def movelets_tree(path_name, label=None):
    movelets = []
    count = 0
    path_to_file = glob.glob(os.path.join(path_name, '**', 'moveletsOnTrain.json'), recursive=True)
    df = pd.DataFrame()
    for path in path_to_file:
        with open(path) as f:
            data = json.load(f)  
            
        if label is not None and label != data[name][0]['label']:
            continue
            
        l = len(data[name])
        for x in range(0, l):
            aux_df = []
            
            points = data[name][x]['points_with_only_the_used_features']
            movelets.append(\
                    Movelet(\
                        count, data[name][x]['trajectory'],\
                        points,\
                        float(data[name][x]['quality']['quality'] * 100.0),\
                        data[name][x]['label'],\
                        int(data[name][x]['quality']['size']))\
                    )
            
            count += 1
        
    return movelets