class Node():
    def __init__(self, value):
        self.value = value
        self.pointer = None

    def __str__(self):
        return f"값: {self.value} 포인터: {self.pointer}"


if __name__ == "__main__":
    a = Node(1)
    print(a)