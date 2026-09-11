from book import Book
from member import Member

class Library():
    books = []
    members = []
    def __init__(self):
        self.name = '한국 도서관'

    def add_books(self): 
        input_id = input("책의 id를 입력하세요. ")
        input_name = input("책의 이름을 입력하세요. ")
        new_book = Book(input_id, input_name)
        Library.books.append(new_book)
        return new_book

    def add_members(self):
        input_m_name = input("회원의 이름을 입력하세요. ")
        input

