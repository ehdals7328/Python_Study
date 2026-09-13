from abc import ABC, abstractmethod
from array_stack import MyStack


if __name__ == "__main__":
    s = MyStack()

    print("\n\nInserted Item: A ")
    s.push("A")
    s.show_stack()

    print("\n\nInserted Item: B ")
    s.push("B")
    s.show_stack()

    print("\n\nInserted Item: C ")
    s.push("C")
    s.show_stack()
    
    print("\n\ndeleted Item: C ")
    s.delete()
    s.show_stack()