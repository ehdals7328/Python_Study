MENU = {'espresso':{"ingredients":{"water": 50, "coffee":18,},"cost":1.5}, 
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee":24}, "cost": 2.5},
        "cappuccino":{"ingredients":{"water":250, "milk":100,"coffee":24},"cost": 3.0}}
profit = 0
resources = {"water":300, "milk": 200, "coffee":100,}

def resources_report(resources, profit): # 리소스를 출력하는 함수
    print("현재 남은 재료 입니다. :")
    print(f"'물' : {resources['water']:}")
    print(f"'우유' : {resources['milk']:}")
    print(f"'커피' : {resources['coffee']:}")
    print(f"기기잔고 {profit:.2f} $")
    return False

def select_drink(): # 사용자로부터 음료를 입력받는 함수
    order = input("어떤 음료를 원하시나요?: [espresso/latte/cappuccino] :")
    order = order.strip() # 입력데이터 전처리
    order = order.lower()

    if order == 'off':
        exit()
    if order == 'report':
        resources_report(resources, profit)
        return False
    if order == 'espresso':
        return 'espresso'
    if order == 'cappuccino':
        return 'cappuccino'
    if order == 'latte':
        return 'latte'
    else:
        print("다시 입력해 주십시오. ")
        return False

def is_resource_sufficient(drink_name, resources): # 입력받은 음료의 재료가 부족한지 확인하는 함수
    coffee = drink_name
    if MENU[coffee]['ingredients']['water'] > resources['water']:
        print("물이 부족합니다.")
        return False      
    elif MENU[coffee]["ingredients"].get("milk", 0) > resources["milk"]:
        print("우유가 부족합니다.")
        return False
    elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print("원두가 부족합니다.")
        return False
    else:
        print("재료가 충분합니다. 음료 제작을 시작합니다. ")
        return True

def process_coins(drink_name, profit): # 동전을 투입
    coins = {"quarters": 0.25, "dimes":0.10, "nickels":0.05, 'pennies':0.01}
    cal = 0
    count_quarters = int(input("쿼터 동전을 넣어주세요. :")) # 돈을 투입하는 과정
    cal = cal + coins["quarters"] * count_quarters
    count_dimes = int(input("다임 동전을 넣어주세요. :"))
    cal = cal + coins["dimes"] * count_dimes
    count_nickels = int(input("니켈 동전을 넣어주세요. :"))
    cal = cal + coins["nickels"] * count_nickels
    count_pennies = int(input("페니 동전을 넣어주세요. :"))
    cal = cal + coins["pennies"] * count_pennies
    return cal
         
def is_transaction_successful(cal, drink_name): # 돈이 충분할때 거래를 하는 함수
    earn = 0
    if cal > MENU.get(drink_name)['cost']:
        exchange = cal - MENU[drink_name]['cost'] # 거스름돈이 있는 주문
        print(f"\n{'=' * 32}\n결제 완료.\n거스름돈 : {exchange:.2f} $ 입니다.\n{'=' * 32}\n여기 주문하신 {drink_name} 가 나왔습니다 ! 즐기세요 :)" )
        earn = MENU.get(drink_name)['cost']
        return earn
    elif cal == MENU.get(drink_name)['cost']: # 거스름돈이 없는 주문
        print(f"\n{'=' * 32}\n결제 완료. \n{'=' * 32}\n여기 주문하신 {drink_name} 가 나왔습니다 ! 즐기세요 :)" )
        earn = MENU.get(drink_name)['cost']
        return earn
    elif cal < MENU.get(drink_name)['cost']: # 돈이 모자랄때 
        print("금액이 모자랍니다. 돈이 환불되었습니다.")
        return False

def make_coffee(drink_name, resources): # resources 를 갱신하는 함수
            resources['water'] = (resources['water'] - MENU[drink_name]["ingredients"]['water'])
            resources['milk'] = (resources['milk'] - MENU[drink_name]["ingredients"].get('milk', 0))
            resources['coffee'] = (resources['coffee'] - MENU[drink_name]["ingredients"]['coffee'])
            return resources

while True:
    drink_name = select_drink() # 1. 음료를 선택 받는다
    if drink_name == False: # 1-1.다른 명령어 ex)Report or 오타 , 처음으로
        continue

    able = is_resource_sufficient(drink_name, resources) # 2.선택 받은 음료의 재료가 충분한지 확인
    if able == False: # 2-1. 재고가 충분하지 않다면 처음으로
        continue

    total_money = process_coins(drink_name, profit) # 3. 동전을 투입

    earn = is_transaction_successful(total_money, drink_name) # 4. 동전을 음료가격과 비교하여 거래 확인
    if earn == False: # 4-1. 돈이 부족하면 처음으로
        continue

    update_resources = make_coffee(drink_name, resources) # 5. 거래가 확인되었으면 재료를 갱신
    if update_resources == False:# 5-5. 재료가 갱신되지 않으면 처음으로
        continue
    resources = update_resources #6. 거래 성사 후 재료 소모값 업데이트
    profit = profit + earn #7. 거래 성사 후 기기 잔액 업데이트
