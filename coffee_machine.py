MENU = {'espresso':{"ingredients":{"water": 50, "milk": 0, "coffee":18,},"cost":1.5}, 
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee":24}, "cost": 2.5},
        "cappuccino":{"ingredients":{"water":250, "milk":100,"coffee":24},"cost": 3.0}}

profit = 0
resources = {
    "water":300, "milk": 200, "coffee":100,
}

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

def able_order(drink_name, resources): # 입력받은 음료의 재료가 부족한지 확인하는 함수
    coffee = drink_name
    if MENU[coffee]['ingredients']['water'] > resources['water']:
        print("물이 부족합니다.")
        return False      
    elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
        print("우유가 부족합니다.")
        return False
    elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print("원두가 부족합니다.")
        return False
    elif MENU[coffee]["ingredients"]["water"] <= resources["water"] and MENU[coffee]["ingredients"]["milk"] <= resources["milk"] and MENU[coffee]["ingredients"]["water"] <= resources["water"]:
        print("재료가 충분합니다. 음료 제작을 시작합니다. ")
        return True

def coin(drink_name, profit): # 동전을 투입
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
    if cal > MENU[drink_name]['cost']:
        exchange = cal - MENU[drink_name]['cost'] # 거스름돈이 있는 주문
        print(f"\n{'=' * 32}\n결제 완료.\n거스름돈 : {exchange:.2f} $ 입니다.\n{'=' * 32}\n여기 주문하신 {drink_name} 가 나왔습니다 ! 즐기세요 :)" )
        earn = MENU[drink_name]['cost']
        return earn
    elif cal == MENU[drink_name]['cost']: # 거스름돈이 없는 주문
        print(f"\n{'=' * 32}\n결제 완료. \n{'=' * 32}\n여기 주문하신 {drink_name} 가 나왔습니다 ! 즐기세요 :)" )
        earn = MENU[drink_name]['cost']
        return earn
    elif cal < MENU[drink_name]['cost']: # 돈이 모자랄때 
        print("금액이 모자랍니다. 돈이 환불되었습니다.")
        return False

def make_coffee(drink_name, able, resources): # resources 를 갱신하는 함수
        if able == True and able != False:
            resources['water'] = (resources['water'] - MENU[drink_name]["ingredients"]['water'])
            resources['milk'] = (resources['milk'] - MENU[drink_name]["ingredients"]['milk'])
            resources['coffee'] = (resources['coffee'] - MENU[drink_name]["ingredients"]['coffee'])
            return resources
        else:
            return
while True:
    drink_name = select_drink()
    if drink_name == False:
        continue

    able = able_order(drink_name, resources)
    if able == False:
        continue
    total_money = coin(drink_name, profit)

    earn = is_transaction_successful(total_money, drink_name)
    if earn == False:
        continue

    update_resources = make_coffee(drink_name, able, resources)
    resources = update_resources
    if make_coffee == False:
        continue

    profit = profit + earn
