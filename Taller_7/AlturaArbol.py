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
 
def height(node):
    if node == None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
 
    return (1 + max(left_height, right_height))
 
 
cantidad_casos = int(input())
valores = []
for caso in range(cantidad_casos):
    
    arbol = BinarySearchTree()
    nodos = list(map(int, input().split(" ")[:-1]))
    for nodo in nodos:
        arbol.insert(nodo)
    valores.append(height(arbol.root))
 
for altura in valores:
    print(altura)