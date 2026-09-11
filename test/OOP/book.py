class Book():
    def __init__(self, id, name): # 책 객체 생성
        self.id = id
        self.name = name

    def __str__(self): # 출력을 보기 쉽게
        return f"책번호:{self.id} 도서명:{self.name}"

    def book_info(self):
        return print(f"책번호:{self.id} 도서명:{self.name}")