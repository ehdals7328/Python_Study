# 도서 관리 프로그램

class Book:
    def __init__(self, name, author, status):
        self.name = name
        self.author = author
        self.status = status

    def show_book(self):
        print(f"제목:{self.name}, 저자:{self.author}, 상태:{self.status}")

    def change_status(self):
        if self.status == '반납':
            self.status = '대여'
        elif self.status == '대여':
            self.status = '반납'
        return self.status
    

class Member:
    def __init__(self, name, id_number, checkout_list):
        self.name = name
        self.number = id_number
        self.checkout_list = checkout_list

    def show_member(self):
        print(f"회원명:{self.name}, 회원ID:{self.number}, 대여중인 도서: {self.checkout_list}")

    def borrow_book(self, name):
        pass

    def return_book(self, name):
        pass


class Library:
    pass
