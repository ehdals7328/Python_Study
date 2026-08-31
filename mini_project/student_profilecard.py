student = {}

name = input("이름을 입력해주세요: ")
age = input("나이를 입력해 주세요: ")
major = input("전공을 입력해 주세요: ")
email = input("이메일을 입력해 주세요: ")
hobbies = input("취미를 입력해 주세요: ")

student['name'] = name
student['age'] = int(age)
student['major'] = major
student['email'] = email
student['hobbies'] = hobbies

key_list = list(student.keys())
value_list = list(student.values())

line = '=' * 34
line_2 = '-' * 34

def profile_print():
    print(line)
    print(f"{' P R O F I L E ':^30}")
    print(line)
    for i in range(len(key_list)):
        print(f"{key_list[i]:<12} {value_list[i]:>18}")
    print(line_2)
    print(f"{'항목수':<12} {len(key_list):>18}개")

def check_profile():
    if text == True: # 항목 검사 제어문
        print(f"{check} 항목이 존재 합니다. value 값은 {student.get(check)} 입니다. ")
    elif text == False:
        print('존재 하지 않는 항목 입니다. ')

check = str(input("다음 항목이 있는지 검사합니다. : "))
text = check in student # 검사를 도와주는 변수
check_profile()

profile_print()