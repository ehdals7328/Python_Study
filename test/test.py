from abc import ABC, abstractmethod


class BookBase(ABC):
    total_books = {}

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_borrowed = False  # 대출 상태 (True: 대출 중, False: 대출 가능)

    def __repr__(self):
            status = "대여중" if self._is_borrowed else "대여가능"
            return f"제목:{self.title} 저자:{self.author} 상태:{status}"

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class PaperBook(BookBase):
    def __init__(self, title, author, location):
        super().__init__(title, author)
        self.location = location

        BookBase.total_books[self.title] = self

    def borrow(self):
        if self._is_borrowed:
            print("현재 대여중인 도서 입니다.")
        else:
            self._is_borrowed = True
            print(f"{self.title} 을(를) 대여 했습니다. ")
            return self._is_borrowed
        
    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"{self.title}을 반납 했습니다. ") 
            return self._is_borrowed
        else:
            print("이미 반납 되어 있는 도서 입니다.")

    def display_info(self):
        if self.is_borrowed:
            status = "대여불가"
        else:
            status = "대여가능"
        print(f"제목:{self.title} 저자:{self.author} 위치:{self.location} 상태:{status}")

class EBook(BookBase):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size
        BookBase.total_books[self.title] = self

    def borrow(self):
        if self._is_borrowed:
            print("현재 보유중인 Ebook 입니다.")
        else:
            self._is_borrowed = True
            print(f"{self.title} 을(를) 다운로드 했습니다. File size : {self.size}MB")
            return self._is_borrowed
        
    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"{self.title} 전자책을 반납 했습니다. ") 
            return self._is_borrowed
        else:
            print("대여하고 있지 않은 Ebook 입니다.")

    def display_info(self):
        if self.is_borrowed:
            status = "대여불가"
        else:
            status = "대여가능"
        print(f"제목:{self.title} 저자:{self.author} filesize:{self.size} 상태:{status}")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # 회원이 대출한 Book 객체들이 저장될 리스트

    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)
        print(f"👤 [{self.name}] 회원의 대출 목록에 '{book.title}'이(가) 추가되었습니다.")

    def remove_borrowed_book(self, book):
        """회원의 대출 목록에서 책 제거"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f" [{self.name}] 회원의 대출 목록에서 '{book.title}'이(가) 반납 처리되었습니다.")

    def show_borrowed_list(self):
        print(f"\n---  {self.name} 회원의 대출 목록 ---")
        if not self.borrowed_books:
            print("현재 대출 중인 도서가 없습니다.")
            return
        
        for idx, book in enumerate(self.borrowed_books, start=1):
            print(f"{idx}. {book.title} ({book.author})")
        print("-----------------------------------")

class Library:
    def __init__(self):
        self.name = '성서 도서관'
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"{self.name}에 {member.name}회원이 등록 되었습니다. ")

    def show_all_books(self):
        for book in BookBase.total_books.values():
            book.display_info()

    def process_borrow(self, title, member):
        if BookBase.borrow():
            member.add_borrowed_book(title)

    def process_return(self, title, member):
        if title.return_book():
            member.remove_borrowed_book(title)

paper = PaperBook('파이썬이 좋아', '노동민', 'A001')
ebook = EBook('C언어가 좋아', '김동민', 28)
user = Member('박상보')

lb = Library()
lb.add_member(user)
lb.show_all_books()