MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000))

print('=' * 50)
print(f"{"M E N U":^50}")
print('=' * 50)
print(f"1.{MENU[0][0]:-<35}{MENU[0][1]:,}원")
print(f"2.{MENU[1][0]:-<35}{MENU[1][1]:,}원")
print(f"3.{MENU[2][0]:-<35}{MENU[2][1]:,}원")
print('=' * 50)

number_menu = []
count = []

number_menu.append(int(input("메뉴 번호를 입력해 주세요 : ")))
count.append(int(input("수량을 입력해 주세요 : ")))
number_menu.append(int(input("메뉴 번호를 입력해 주세요 : ")))
count.append(int(input("수량을 입력해 주세요 : ")))

print('=' * 50)
print(f"{"영 수 증":^50}")
print('=' * 50)
print(f"{MENU[number_menu[0] - 1][0]} {count[0]}개 {MENU[number_menu[0] - 1][1] * count[0]:>30,}원")
print(f"{MENU[number_menu[1] - 1][0]} {count[1]}개 {MENU[number_menu[1] - 1][1] * count[1]:>30,}원")
print('-' * 50)
print(f"주문 금액{MENU[number_menu[0] - 1][1] * count[0] + MENU[number_menu[1] - 1][1] * count[1]:>30,}원")
print(f"부가세(10%){(MENU[number_menu[0] - 1][1] * count[0] + MENU[number_menu[1] - 1][1] * count[1]) * 0.1:>30,.0f}원")
print(f"결제 금액 {(MENU[number_menu[0] - 1][1] * count[0] + MENU[number_menu[1] - 1][1] * count[1]) + 
               ((MENU[number_menu[0] - 1][1] * count[0] + MENU[number_menu[1] - 1][1] * count[1]) * 0.1):>30,.0f}원")
print('=' * 50)