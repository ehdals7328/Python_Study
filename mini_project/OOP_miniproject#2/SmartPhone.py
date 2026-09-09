from Address import Addr, CompanyAddr, CustomerAddr
from SmartPhoneMain import SmartPhoneMain

class SmartPhone():
    def __init__(self):
        self.Phone_name = '스마트폰'
        self.contact = []
        self.sorted_contact  = []

    def inputAddrData(self):
        print("# 연락처 등록(회사)")        
        input_name = input("이름을 입력하세요: ")
        input_phone = input("전화번호를 입력하세요: ")
        input_email = input("이메일을 입력하세요: ")
        input_address = input("주소를 입력하세요: ")
        input_birth = input("생일을 입력하세요: ")
        input_co_name = input("회사명을 입력하세요: ")
        input_part = input("부서 이름을 입력하세요: ")
        input_rank = input("직급을 입력하세요: ")
        person = CompanyAddr(input_name, input_phone, input_email, input_address, input_birth, '회사', input_co_name, input_part, input_rank)
        return person

    def inputAddrData_2(self):
        print("# 연락처 등록(거래처)")        
        input_name = input("이름을 입력하세요: ")
        input_phone = input("전화번호를 입력하세요: ")
        input_email = input("이메일을 입력하세요: ")
        input_address = input("주소를 입력하세요: ")
        input_birth = input("생일을 입력하세요: ")
        input_cu_name = input("거래처명을 입력하세요: ")
        input_item = input("품목 이름을 입력하세요: ")
        input_rank = input("직급을 입력하세요: ")
        person = CustomerAddr(input_name, input_phone, input_email, input_address, input_birth, '거래처', input_cu_name, input_item, input_rank)
        return person

    def addAddr(self, person):
        self.contact.append(person)
        print("=" * 25)
        print(f"데이터가 저장되었습니다. (현재 {len(self.contact)}개)")
        print("-" * 25)

    def printAddr(self, person):
        print(f"저장된 데이터 :{person}")
        print("=" * 25)

    def printAllAddr(self, contact):
        print("=" * 25)
        print(f"{'모든 연락처':^23}")
        print("=" * 25)
        for idx, obj in enumerate(contact, start=1):
            print(f"{idx} {obj}")
        print("=" * 25)

    def searchAddr(self):
        input_s = input("\n검색할 전화번호를 입력해 주세요. :")
        for obj in self.contact:
            if obj.phone == input_s:
                print(f"\n검색결과: [{obj}] \n")
                return True
        print("없는 전화번호 입니다.")
        return False

    def deletedAddr(self):
        input_d = input("\n삭제할 전화번호를 입력해 주세요. :")
        for obj in self.contact:
            if obj.phone == input_d:
                self.contact.remove(obj)
                print(f"{obj.name}님의 연락처가 삭제 되었습니다. ")
                return True
        print("없는 전화번호 입니다.")
        return False

    def editAddr(self):
        input_e = input("\n수정할 대상의 이름을 입력해 주세요. :")
        for obj in self.contact:
            if obj.name == input_e:
                change_phone = input(f"새 전화번호를 입력해 주세요. (현재번호:{obj.phone})   :")
                obj.phone = change_phone
                print(f"\n{obj.name}님의 연락처가 변경 되었습니다. (변경된번호:{change_phone})")
                return True
        print("없는 이름 입니다.")
        return False

    def sort_list(self):
        self.sorted_contact = sorted(self.contact, key=lambda x: x.name)
        return self.sorted_contact

adress2 = Addr('하철수', '010-1111-2222', 'cjftn1111@gmail.com', '서울', '가족', '1101')
adress3 = Addr('김영희', '010-3333-4444', 'dudgml3333@gmail.com', '부산', '가족', '0101')

main = SmartPhoneMain()
s_p = SmartPhone()

s_p.contact.append(adress2)
s_p.contact.append(adress3)

if __name__ == "__main__":
    while True:
        input("메뉴를 불러오려면 enter를 입력하세요.")
        num = main.print_menu()
        if num == '1':
            obj = s_p.inputAddrData()
            s_p.addAddr(obj)
            s_p.printAddr(obj)

        elif num == '2':
            obj = s_p.inputAddrData_2()
            s_p.addAddr(obj)
            s_p.printAddr(obj)
        
        elif num == '3':
            s_p.printAllAddr(s_p.sort_list())

        elif num == '4':
            s_p.searchAddr()

        elif num == '5':
            s_p.deletedAddr()      

        elif num == '6':
            s_p.editAddr()

        elif num == '7':
            print("프로그램을 종료 합니다. ")
            exit()

        else:
            print("잘못된 번호 입니다. 다시 입력해 주세요 (1-7)")
            continue     
