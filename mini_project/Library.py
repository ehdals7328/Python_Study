# 260908 도서관 대출 관리 시스템
from abc import ABC, abstractmethod
from collections import Counter

class LibraryItem(ABC):
    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_loaned = False # 대출 가능이란 뜻
        self.borrower = None # 대여자
        LibraryItem.total_items += 1

    def __str__(self):
        return f"{self.title}"

    @abstractmethod
    def loan_period(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def checkout(self, name):
        if not self.is_loaned:
            print(f"{name}님, '{self.title}'대출 완료! (대출 기간 {self.loan_period()}일)")
            self.is_loaned = True # 대여 불가 상태로 전환
            self.borrower = name
            return True
        else:
            print(f"'{self.title}'은(는) 이미 {self.borrower}님이 대출 중입니다.")
            return False

    def return_item(self):
        if self.is_loaned:
            print(f"{self.borrower}님, '{self.title}' 반납 완료!")
            self.is_loaned = False # 대여 가능 상태로 전환
            self.borrower = None # 대여자 이름 삭제
            return True
        else:
            print(f"'{self.title}'은(는) 이미 반납 되어 있습니다.")
            return False

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서]{self.title} / {self.author} / {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD]{self.title} / {self.director} 감독 / {self.minutes}분"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지]{self.title} / {self.issue}호"

class Library:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)
        return print(f"'{item}'등록 완료 (총{len(self.items)}개)")

    def find(self, item_id):
        for a in self.items:
            if a.item_id == item_id:
                return a        
        print("해당 자료는 없습니다.")
        return None

    def show_all(self):
        state = None
        print("=" * 56)
        print(f"{self.name:^25}")
        print("=" * 56)
        print(f"{'id'} {'정보'} {'상태'}")
        print("-" * 56)
        if not self.items:
            print("현재 도서가 없습니다.")
            return False
        for line in self.items:
            if not line.borrower:
                state = '대출가능'
            else:
                state = f'대출중 대여자:{line.borrower}님'
            print(f"{line.info()}, {state}")
        print("=" * 56)

    def report(self):
        result = Counter(type(obj).__name__ for obj in self.items)
        print("-" * 56)
        print(f"{'종류별 등록 현황'}")
        print("-" * 56)
        for line in result:
            print(f"{line:<} {result[line]}개")
        print("-" * 56)
        print(f"대출중 {len([i for i in self.items if i.is_loaned])}개")
        print(f"전체등록 {LibraryItem.total_items}개")
        
        
        
   
book1 = Book("책1", "A000", "김민수", '100쪽')
dvd1 = DVD("영화1", "A001", "놀란", '169')
magazine1 = Magazine("잡지1", "A002", '3')
lib1 = Library("한빛도서관")
lib1.add(book1)
lib1.add(dvd1)
lib1.add(magazine1)

while True:
    print("1.전체목록 2.통계 3.대출 4.반납 0.종료")
    select = int(input("번호를 선택 하세요: "))
    if select == 1:
        lib1.show_all()

    elif select == 2:
        lib1.report()

    elif select == 3:
        loan_num = input("대출하실 책의 id를 입력해 주세요.")
        name = input("대여자 이름")
        object = lib1.find(loan_num)
        object.checkout(name)

    elif select == 4:
        loan_num = input("반납하실 책의 id를 입력해 주세요.")
        object2 = lib1.find(loan_num)
        object2.return_item()

    elif select == 0:
        print("종료합니다.")
        exit()

    else:
        print("없는 번호 입니다.")

    