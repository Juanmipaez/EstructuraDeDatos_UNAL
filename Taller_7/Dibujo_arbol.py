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

def nivelNodo(root, node):
    contador = 0

    if root == None or root.key==node:
        return 0
    
    if node < root.key:
        contador+=1
        left_tree = nivelNodo(root.left, node)
        return (contador + left_tree)
    else:
        contador+=1
        right_tree = nivelNodo(root.right, node)
        return (contador+right_tree)

cantidad_casos = int(input())

arboles = []

for caso in range(cantidad_casos):
    nodos = list(map(int, input().split(" ")[:-1]))
    arboles.append(nodos)

for arbol in arboles[:-1]:
    arbol_binario = BinarySearchTree()
    for nodo in arbol :
        arbol_binario.insert(nodo)
    arbol.sort(reverse=True)
    
    for elemento in arbol:
        print(f'{nivelNodo(arbol_binario.root,elemento)*8*" "}{elemento}')
    print()

arbol = arboles[-1]
arbol_binario = BinarySearchTree()
for nodo in arbol :
    arbol_binario.insert(nodo)
arbol.sort(reverse=True)

for elemento in arbol:
    print(f'{nivelNodo(arbol_binario.root,elemento)*8*" "}{elemento}')
