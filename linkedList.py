class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.totalElements = 0

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None

    def add(self, data: int) -> None:
        newNode = self.Node(data)
        newNode.next = None

        if self.head == None:
            self.head = newNode
        else:
            last = self.getLastNode()
            last.next = newNode

        self.totalElements += 1

    def getLastNode(self) -> Node:
        if self.head == None:
            return None

        last = self.head
        control = self.head

        while control != None:
            last = control
            control = last.next

        return last

    def getNodeAt(self, position: int) -> Node:
        if self.head == None or (self.totalElements - 1) < position:
            return None

        control = self.head
        x = 0

        while control != None:
            if x == position:
                break
            x += 1
            control = control.next

        return control

    def appendElement(self, node: Node, data: int) -> None:
        if self.head == None or node == None:
            return

        newNode = self.Node(data)
        previous = node
        next = node.next

        previous.next = newNode
        newNode.next = next
        self.totalElements += 1

    def delete(self, node: Node) -> None:
        if self.head == None or node == None:
            return
        control = self.head
        temp = None

        if node == self.head:
            temp = self.head
            self.head = self.head.next

            temp = None
        else:
            while control.next != node:
                control = control.next

            temp = control.next
            control.next = temp.next
            temp = None
        self.totalElements -= 1

    def show(self) -> None:
        node = self.head
        while node != None:
            print("*", node.data)
            node = node.next


linkedList = LinkedList()
linkedList.add(5)
linkedList.add(10)
linkedList.add(15)
linkedList.add(20)

linkedList.appendElement(linkedList.getNodeAt(1), 30)
linkedList.delete(linkedList.getNodeAt(4))

linkedList.show()
