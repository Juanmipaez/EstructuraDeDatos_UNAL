from collections import deque

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))

        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def delete(self, key):
        self.size -= self.search(key)
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._getMin(root.right)
            root.key = temp
            root.right = self._deleteRecursively(root.right, temp)
        if root is None:
            return root

        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        balanceFactor = self._getNodeBalance(root)

        if balanceFactor > 1:
            if self._getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self._getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height

    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)

    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)

    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements
    
    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def PosOrder(self):
        elements = []
        self._PosOrderRecursively(self.root, elements)
        return elements

    def _PosOrderRecursively(self, root, elements):
        if root:
            self._PosOrderRecursively(root.left, elements)
            self._PosOrderRecursively(root.right, elements)
            elements.append(root.key)
            
def fun_nivel(root, key, nivel):
    if root is None:
        return -1
    if root.key == key:
        return nivel
    left_level = fun_nivel(root.left, key, nivel + 1)
    if left_level != -1:
        return left_level
    return fun_nivel(root.right, key, nivel + 1)

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

casos = int(input())

arboles = []
for caso in range(casos):

    secuencia_fib = [1,2]
    longitud_secuencia = int(input())
    for i in range(longitud_secuencia-2):
        suma = secuencia_fib[-1] + secuencia_fib[-2]
        secuencia_fib.append(suma)
    arboles.append(secuencia_fib)

for arbol in arboles[:-1]:
    arbol_binario = AVLTree()
    for nodo in arbol :
        arbol_binario.insert(nodo)
    arbol.sort(reverse=True)
    
    for elemento in arbol:
        print(f'{nivelNodo(arbol_binario.root,elemento)*8*" "}{elemento}')
    print()

arbol = arboles[-1]
arbol_binario = AVLTree()
for nodo in arbol :
    arbol_binario.insert(nodo)
arbol.sort(reverse=True)

for elemento in arbol:
    print(f'{nivelNodo(arbol_binario.root,elemento)*8*" "}{elemento}')
