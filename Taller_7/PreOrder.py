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
    
    def PreOrder(self):
        elements = []
        self._PreOrderRecursively(self.root, elements)
        return elements
    
    def _PreOrderRecursively(self, root, elements):
        if root:
            elements.append(root.key)
            self._PreOrderRecursively(root.left, elements)
            self._PreOrderRecursively(root.right, elements)

cantidad_casos = int(input())
valores = []

for casos in range(cantidad_casos):
    arbol = BinarySearchTree()
    datos = input().split(" ")[:-1]

    for s in datos:
        arbol.insert(int(s))
    valores.append(''.join(map(str, arbol.PreOrder())))

for p in valores:
    print(p)