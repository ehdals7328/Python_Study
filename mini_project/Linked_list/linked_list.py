from node import Node

class LinkedList():

    def __init__(self):
        self.name = 'single Linked List'
        self.head = None # 시작 노드를 의미
        self.tail = None # 끝 노드를 의미

    def add_node(self, value):
        new_node = Node(value)

        if self.head is None: # 데이터가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else: # 데이터가 있는 경우
            self.tail.pointer = new_node
            self.tail = new_node


    def find_node(self, location, value):
        current = self.head
        while current:
            if current.value == location:
                new_node = Node(value)
                new_node.pointer = current.pointer
                current.pointer = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.pointer
        print(f"{location}는(은) 없는 값 입니다. ")


    def show_list(self):
        current = self.head
        while current:
            print(f"{current.value}", end=' ---> ')
            current = current.pointer    
        print("None")

    def sort_rev(self):
        current = self.head
        prev = None
        self.tail = self.head

        while current:
            next_node = current.pointer # 다음 위치를 기억
            current.pointer = prev # 현재 포인터를 뒤로
            prev = current # 과거는 현재로
            current = next_node # 현재는 미래로

        self.head = prev

    def del_node(self, location):
        if self.head is None: # 삭제할 값이 없는 경우
            print("현재 리스트가 비어있습니다.")
            return

        if self.head.value == location: # 삭제할 값이 첫번째인 경우
            self.head = self.head.pointer
            if self.head is None: # 마지막 값을 삭제한 경우
                self.tail = None
            return

        current = self.head
        while current.pointer:
            if current.pointer.value == location:
                if current.pointer == self.tail: # 꼬리 갱신
                    self.tail = current

                current.pointer = current.pointer.pointer
                return
            current = current.pointer
        print("잘못 된 노드(위치) 값 입니다.")


if __name__ == "__main__":

    ll = LinkedList()

    print("[1번] 공백 리스트에 노드 3개 삽입하기. ")
    ll.show_list()
      
    for i in range(3):
        input_add = int(input("연결 리스트에 추가할 값을 입력 하세요. "))
        ll.add_node(input_add)
        ll.show_list()
    
    print("[2번] 3 노드 뒤에 5 노드 삽입하기. ")
    ll.show_list()
    input_index = int(input("어느 노드 뒤에 삽입 하시겠습니까?"))
    input_node = int(input("어떤 값을 삽입 하시겠습니까?")) 
    ll.find_node(input_index, input_node)
    print(f"{input_index}뒤에 {input_node}를 삽입 했습니다.")
    ll.show_list()

    moment = input("\n[3번] 리스트의 노드를 역순으로 바꾸기. ( 바꾸려면 enter )")
    ll.sort_rev()
    ll.show_list()

    print("[4번] 리스트의 마지막 노드 삭제하기")
    ll.show_list()
    input_del = int(input("어떤 노드를 삭제 하시겠습니까?"))
    ll.del_node(input_del)
    ll.show_list()
    