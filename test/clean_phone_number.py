#전화번호를 '-' 없이 입력받고 '-'을 포함하여 출력하는 함수

def clean_num():
    input_number = input("전화번호를 입력해 주세요 (- 기호 없이 입력 하세요)")
    if len(input_number) == 11:
        zero = input_number[:3]
        middle = input_number[3:7]
        last = input_number[7:]
        result = f"{zero}-{middle}-{last}"
        return result
    else:
        print("다시 입력해 주세요. ")

a = clean_num()
print (a)