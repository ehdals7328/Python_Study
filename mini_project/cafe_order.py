MENU = (('아메리카노', 4500), ('카페라떼', 5000), ('녹차', 4000)) # 메뉴판은 튜플로 고정

number_menu = [] # 메뉴를 받을 리스트
count = [] # 갯수를 받을 리스트

line = '=' * 50 # 영수증 출력 라인
line_2 = '-' * 50 # 영수증 출력 라인2

def show_menu(): # 메뉴판 함수
    print(line)
    print(f"{'M E N U':^50}")
    print(line)
    for j in range(len(MENU)): # 메뉴판 출력 MENU의 0번 인덱스는 메뉴이름, 1번 인덱스는 가격
        print(f"{j+1}.{MENU[j][0]:-<35}{MENU[j][1]:,}원") # 1천단위 구분
    print(line)

def bill(): # 영수증 함수
    total = 0 # 합계를 계산하기 위한 빈 변수
    print(line)
    print(f"{'영 수 증':^50}")
    print(line)
    for i in range(len(number_menu)): # number_menu의 길이만큼 반복
        order_1 = MENU[number_menu[i] - 1][1] * count[i]
        total = total + order_1 # 첫 계산을 마치면 order_1 에서 계산된 값을 total에 누적
        print(f"{MENU[number_menu[i] - 1][0]} {count[i]}개 {order_1:>30,}원") 
    print(line_2)
    print(f"주문 금액{total:>30,}원")
    print(f"부가세(10%){total * 0.1:>30,.0f}원")
    print(f"결제 금액 {total + (total * 0.1):>30,.0f}원")
    print(line)

show_menu()

for order in range(2):
    number_menu.append(int(input("주문하실 메뉴를 선택해 주세요 :")))
    count.append(int(input("주문하실 수량을 입력해 주세요 :")))

bill()