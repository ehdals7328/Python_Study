from abc import ABC, abstractmethod
from node import Node

class Stack(ABC): # 추상클래스 ABC를 상속받는 구조

    @abstractmethod
    def is_empty(self) -> bool:
        pass
    @abstractmethod
    def push(self, item: str) -> None:
        pass
    @abstractmethod
    def pop(self) -> str:
        pass
    @abstractmethod
    def delete(self) -> None:
        pass
    @abstractmethod
    def peek(self) -> str:
        pass


class MyStack(Stack): # Stack 클래스를 상속받는 구조
    def __init__(self):
        self.name = "MyStack"
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True # 비어있음 
        else:
            return False # 값이 있음

    def push(self, item): # item's type =  str
        new_node = Node(item)
        new_node.pointer = self.top
        self.top = new_node

    def pop(self):
        poped = None
        if self.is_empty() is True:
            print("값이 없습니다.")
        else:
            poped = self.top.value
            self.top = self.top.pointer
            return poped

    def delete(self):
        self.pop()

    def peek(self):
        if self.is_empty() is True:
            print("값이 없습니다.")
        else:
            return self.top.value

    def show_stack(self):
        current = self.top
        stack = []
        print("Array Stack>> ", end=' ')
        while current:
            stack.append(current.value)
            current = current.pointer
        sorted_stack = stack[::-1]
        for i in sorted_stack:
            print(f"{i}", end=' ')
