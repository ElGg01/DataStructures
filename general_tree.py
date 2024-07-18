class TreeNode:
    def __init__(self, data: str) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, indentation: int) -> None:

        spaces = " " * self.get_level() * indentation
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree(indentation)


def build_product_tree() -> TreeNode:
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree(3)


if __name__ == "__main__":
    build_product_tree()
