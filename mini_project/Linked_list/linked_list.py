class Node():
    L = ()
    def __init__(self, value):
        self.value = value
        self.point = None

    def __str__(self):
        return f"값:{self.value}, 포인터: {self.point}"


    def add_node(value):
        new_node = Node(value)
        return new_node
