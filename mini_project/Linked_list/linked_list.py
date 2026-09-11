class Node():
    L = ()
    def __init__(self, value):
        self.value = value
        self.point = None

    def __str__(self):
        return f"값:{self.value}, 포인터: {self.point}"

    def add_node(self, value):
        new_node = Node(value)
        self.point = new_node.value

a = Node(1)
print(a)