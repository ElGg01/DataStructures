class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add(self, element: int):
        print("Element added: ", element)
        self.stack.append(element)

    def remove(self) -> int:
        print("Element: ", self.stack[-1], " ", "removed")
        return self.stack.pop()

    def show(self):
        print("")
        for element in self.stack:
            print("│", element, "│")
        print("─────")


stack = Stack()
stack.add(5)
stack.add(10)
stack.show()
stack.remove()
stack.show()
