def map(tree: node, route:str, code:dict)
    if isleaf(tree:
              code.add(tree.char, route))
    else:
        map(tree.left, route +"0", code)
        map(tree.right, route +"1", code)

def createMap(Tree:node):
    code = {}
    map(tree,"",code)
    return code