class Stack:
    def __init__(self) -> None:
        pass

    stack = []

    def add(self, element: int):
        self.stack.append(element)

    def remove(self) -> int:
        return self.stack.pop()

    def show(self):
        print(self.stack)


stack = Stack()
stack.add(5)
stack.add(10)
stack.remove()
stack.show()
