class Node:
    def __init__(self, value: int) -> None:
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.value = value


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def showBinaryTree(self, indentation: int = 4) -> None:
        if self.root == None:
            print("Tree empty")
            return

        def traverseBinaryTree(node: Node, string: str) -> None:
            print(str(node.value))
            # Left child:
            if node.left_child != None:
                if node.right_child != None:
                    print(string + "├" + "─" * indentation, end="")
                else:
                    print(string + "└" + "─" * indentation, end="")
                traverseBinaryTree(node.left_child, string + "│" + " " * indentation)
            if node.right_child != None:
                print(string + "└" + "─" * indentation, end="")
                traverseBinaryTree(node.right_child, string + "│" + " " * indentation)

        traverseBinaryTree(self.root, "")

    # METHODS FOR BST TREE

    def insert(self, value: int) -> None:
        y = None
        x = self.root
        n = Node(value)

        while x != None:
            y = x
            if n.value <= x.value:
                x = x.left_child
            else:
                x = x.right_child

        n.parent = y

        if y == None:
            self.root = n
        else:
            if n.value <= y.value:
                y.left_child = n
            else:
                y.right_child = n

    def showBST(self, indentation: int = 4) -> None:
        if self.root == None:
            print("Empty tree")
            return

        def transverseBST(node: Node, string: str) -> None:
            print(str(node.value))
            if node.left_child != None:
                if node.right_child != None:
                    print(string + "├" + "─" * indentation, end="")
                    transverseBST(node.left_child, string + "│" + " " * indentation)
                else:
                    print(string + "└" + "─" * indentation, end="")
                    transverseBST(node.left_child, string + " " * (indentation + 1))

            if node.right_child != None:
                print(string + "└" + "─" * indentation, end="")
                transverseBST(node.right_child, string + " " * (indentation + 1))

        transverseBST(self.root, "")

    def search(self, value: int) -> Node:
        node = self.root
        while node != None and node.value != value:
            if value < node.value:
                node = node.left_child
            else:
                node = node.right_child
        return node


# TEST
tree = BinaryTree()

node1 = Node(5)
tree.root = node1

node2 = Node(100)
node1.left_child = node2
node2.parent = node1

node3 = Node(3)
node3.parent = node1
node1.right_child = node3

node4 = Node(20)
node4.parent = node2
node2.left_child = node4

node5 = Node(10)
node5.parent = node2
node2.right_child = node5

node6 = Node(7)
node6.parent = node4
node4.left_child = node6

node7 = Node(4)
node7.parent = node4
node4.right_child = node7

tree.showBinaryTree()


# Get the level of a node
def getNodeLevel(node: Node) -> None:
    if node.parent == None:
        return 0
    else:
        return 1 + getNodeLevel(node.parent)


print("Nivel del nodo: " + str(getNodeLevel(node7)))


def getTreeHeight(tree: BinaryTree) -> int:

    def getHeight(node: Node) -> int:
        if node == None:
            return -1
        else:
            return 1 + max(getHeight(node.left_child), getHeight(node.right_child))

    return getHeight(tree.root)


print("Altura del arbol: " + str(getTreeHeight(tree)))


def getTreeNodes(tree: BinaryTree) -> int:

    def getTotalNodes(node: Node) -> int:
        if node == None:
            return 0
        else:
            return 1 + getTotalNodes(node.left_child) + getTotalNodes(node.right_child)

    return getTotalNodes(tree.root)


print("Numero total de nodos: " + str(getTreeNodes(tree)))


# Create Binary search trees
def createBST(array: list) -> BinaryTree:
    bst = BinaryTree()
    for i in array:
        bst.insert(i)
    return bst


print("ARBOL BST:")

array = [5, 1, 4, 7, 8, 2, 9, 0, 3, 6]
bst = createBST(array)
bst.showBST()


# SEARCH:
valueToSearch = 8
a = bst.search(valueToSearch)
if a != None:
    print(f"Se encontro el valor {valueToSearch} en el arbol")
else:
    print(f"No existe el elemento {valueToSearch} en el arbol")
