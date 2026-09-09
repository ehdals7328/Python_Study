from Address import Addr
from SmartPhoneMain import SmartPhoneMain

class SmartPhone():
    list = []
    def __init__(self):
        self.Phone_name = '스마트폰'

    def __str__(self):
        return f"{self.name} {self.phone} {self.email} {self.adress} {self.group}"

    def inputAddrData(self):
        input_name = input("이름을 입력하세요: ")
        input_phone = input("전화번호를 입력하세요: ")
        input_email = input("이메일을 입력하세요: ")
        input_address = input("주소를 입력하세요: ")
        input_group = input("그룹(친구/가족)을 입력하세요: ")
        person = Addr(input_name, input_phone, input_email, input_address, input_group)
        return person

    def addAddr(self, person):
        SmartPhone.list.append(person)
        print("데이터가 저장되었습니다.")

    def printAddr(self, person):
            print(f"{person}")

    def printAllAddr(self, list):
        for idx, obj in enumerate(list, start=1):
            print(f"{idx} {obj}")

    def searchAddr(self, search_obj):
        for obj in SmartPhone.list:
            if obj.phone == search_obj:
                return obj
        return False

    def deleteAddr(self, delete_obj):
        for obj in SmartPhone.list:
            if obj.phone == delete_obj:
                SmartPhone.list.remove(obj)
                return obj
        return False

    def editAddr(self, search_name):
        for obj in SmartPhone.list:
            if obj.name == search_name:
                change_phone = input(f"새 전화번호를 입력해 주세요. 현재번호:{obj.phone}:")
                obj.phone = change_phone
                return obj
        return False

adress2 = Addr('김철수', '010-1111-2222', 'cjftn1111@gmail.com', '서울', '가족')
adress3 = Addr('최영희', '010-3333-4444', 'dudgml3333@gmail.com', '부산', '가족')

SmartPhone.list.append(adress2)
SmartPhone.list.append(adress3)

main = SmartPhoneMain()
s_p = SmartPhone()

if __name__ == "__main__":
    while True:
        num = main.print_menu()
        if num == '1':
            object = s_p.inputAddrData()
            s_p.addAddr(object)
            s_p.printAddr(object)

        elif num == '2':
            s_p.printAllAddr(SmartPhone.list)

        elif num == '3':
            find_phone = input("검색할 연락처를 입력해 주세요 :")
            searched_obj = s_p.searchAddr(find_phone)
            if not searched_obj:
                print("없는 연락처 입니다.")
                continue
            print(f"검색결과: {searched_obj}")

        elif num == '4':
            del_phone = input("삭제할 연락처를 입력해 주세요 :")
            deleted_obj = s_p.deleteAddr(del_phone)
            if not deleted_obj:
                print("없는 연락처 입니다.")
                continue            
            print(f"{deleted_obj.name}님의 연락처가 삭제 되었습니다. ")

        elif num == '5':
            edit_phone = input("연락처를 수정할 이름을 입력해 주세요. :")
            edited_obj = s_p.editAddr(edit_phone)
            if not edited_obj:
                print("잘못된 이름 입니다.")
                continue

            print(f"{edited_obj.name}님의 연락처가 변경 되었습니다 {edit_phone}. ")

        elif num == '6':
            print("프로그램을 종료 합니다. ")
            exit()

        else:
            print("다시 입력해 주세요. ")
            continue     
