MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000))

print('=' * 50)
print(f"{'M E N U':^50}")
print('=' * 50)
print(f"1.{MENU[0][0]:-<35}{MENU[0][1]:,}원")
print(f"2.{MENU[1][0]:-<35}{MENU[1][1]:,}원")
print(f"3.{MENU[2][0]:-<35}{MENU[2][1]:,}원")
print('=' * 50)

number_menu = []
count = []
e = '=' * 50

for order in range(2):
    number_menu.append(int(input("주문하실 메뉴를 선택해 주세요 :")))
    count.append(int(input("주문하실 수량을 입력해 주세요 :")))

def bill():
    total = 0
    print(e)
    print(f"{'영 수 증':^50}")
    print(e)
    for i in range(len(number_menu)):
        order_1 = MENU[number_menu[i] - 1][1] * count[i]
        total = total + order_1
        print(f"{MENU[number_menu[i] - 1][0]} {count[i]}개 {MENU[number_menu[i] - 1][1] * count[i]:>30,}원")
    print('-' * 50)
    print(f"주문 금액{total:>30,}원")
    print(f"부가세(10%){total * 0.1:>30,.0f}원")
    print(f"결제 금액 {total + (total * 0.1):>30,.0f}원")
    print(e)

bill()
# 1) print 안에서 계산을 전부 해결하지 말고 변수로 만들어서 시도해보기
# 2) 주문을 입력받는 갯수를 반복문으로 처리해보기
# 3) 영수증 프린트를 하나의 함수로 만들어보기