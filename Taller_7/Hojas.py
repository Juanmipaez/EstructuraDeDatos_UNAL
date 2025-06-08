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

def hojas(node):
    if node == None:
        return 0
    if ((node.left == None) and (node.right== None)):
        return 1
    left_tree = hojas(node.left)
    right_tree = hojas(node.right)

    return (left_tree+right_tree)

cantidad_casos = int(input())
valores = []

for casos in range(cantidad_casos):
    arbol = BinarySearchTree()
    datos = input().split(" ")[:-1]
    for s in datos:
        arbol.insert(int(s))
    valores.append(hojas(arbol.root))

for p in valores:
    print(p)