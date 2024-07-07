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
                    print(string + "L" + "-" * indentation, end="")
                else:
                    print(string + "L" + "-" * indentation, end="")
                traverseBinaryTree(node.left_child, string + "|" + " " * indentation)
            if node.right_child != None:
                print(string + "L" + "-" * indentation, end="")
                traverseBinaryTree(node.right_child, string + "|" + " " * indentation)

        traverseBinaryTree(self.root, "")


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
