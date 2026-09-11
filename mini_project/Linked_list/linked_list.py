from node import Node

class LinkedList():

    def __init__(self):
        self.name = 'sigle linked list'
        self.past_node = None
        self.start = None

    def add_node(self, new_node):
        if self.past_node == None:
            self.past_node = Node(new_node)
            self.start = self.past_node
        else:
            self.past_node.pointer = Node(new_node)
            self.past_node = self.past_node.pointer

    def find_node(self, location, value):
        check_list = self.start
        try:
            while True:
                if check_list.value == location:
                    temp = check_list.pointer
                    check_list.pointer = Node(value)
                    check_list.pointer.pointer = temp
                    return
                else:
                    check_list = check_list.pointer
        except AttributeError:
            pass      

    def show_list(self, index):
        try:
            while True:
                print(f"{index.value}", end=' ---> ')
                index = index.pointer    
        except AttributeError:
            print("None")

    def sort_rev(self):
        sorted_list = self.start
        past_addr = None
        next_addr = None

        while True:
            next_addr = sorted_list.pointer
            sorted_list.pointer = past_addr
            past_addr = sorted_list
            sorted_list = next_addr
            if next_addr == None:
                break
            self.start = sorted_list

    def del_node(self, location):
        index = self.start
        if index.value == location:
            self.start = index.pointer
            return
        while True:
            if index.pointer.value == location:
                temp = index
                index = index.pointer
                temp.pointer = index.pointer
                return
            index = index.pointer

ll = LinkedList()
index = ll.start

if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n[1번] 공백 리스트에 노드 3개 삽입하기. ")
    ll.show_list(ll.start)
    for i in range(3):
        input_add = int(input("연결 리스트에 추가할 값을 입력 하세요. "))
        ll.add_node(input_add)
        ll.show_list(ll.start)
    print("\n\n\n\n\n\n\n\n\n\n\n[2번] 3 노드 뒤에 5 노드 삽입하기. ")
    ll.show_list(ll.start)
    input_index = int(input("어느 노드 뒤에 삽입 하시겠습니까?"))
    input_node = int(input("어떤 값을 삽입 하시겠습니까?")) 
    ll.find_node(input_index, input_node)
    print(f"{input_index}뒤에 {input_node}를 삽입 했습니다.")
    ll.show_list(ll.start)
    moment = input("\n[3번] 리스트의 노드를 역순으로 바꾸기. ( 바꾸려면 enter )")
    ll.sort_rev()
    ll.show_list(ll.start)
    print("\n\n\n\n\n\n\n\n\n\n\n[4번] 리스트의 마지막 노드 삭제하기")
    ll.show_list(ll.start)
    input_del = int(input("어떤 노드를 삭제 하시겠습니까?"))
    ll.del_node(input_del)
    ll.show_list(ll.start)
    