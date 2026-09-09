class SmartPhoneMain:
    def print_menu(self):
        print("\n주소관리 메뉴")
        print("-" * 25)
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        print("-" * 25)
        select = input("원하는 작업을 선택하세요 (1-6): ")
        return select
