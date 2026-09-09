class SmartPhoneMain:
    def print_menu(self):
        print("\nContact Manager")
        print("-" * 25)
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4. 연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        print("-" * 25)
        select = input("원하는 작업을 선택하세요 (1-7): ")
        return select
