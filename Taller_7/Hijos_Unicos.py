class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)
 
    def _insertRecursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root
 
def hijos_unicos(node):
    count = 0
    if node == None:
        return 0
    
    if ( ((node.left is not None) and (node.right is None)) or ((node.left is None) and (node.right is not None)) ):
        count +=1
    
    left_tree = hijos_unicos(node.left)
    right_tree = hijos_unicos(node.right)
 
    return (count+ left_tree+right_tree)
 
cantidad_casos = int(input())
valores = []
 
for casos in range(cantidad_casos):
    arbol = BinarySearchTree()
    datos = input().split(" ")[:-1]
    for s in datos:
        arbol.insert(int(s))
    valores.append(hijos_unicos(arbol.root))
 
for p in valores:
    print(p)