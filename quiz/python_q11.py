name = input("이름을 입력하세요: ")
year = input("태어난 해를 입력하세요: ")

int_year = int(year)
old = 2026 - int_year + 1
print(type(name), type(year))
print(f"{name} 님은 올해 {old}살 입니다.")
print(f"{name} 님의 내년 나이는 {old + 1} 살 입니다.")