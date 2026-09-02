MENU = {'espresso':{"ingredients":{"water": 50, "milk": 0, "coffee":18,},"cost":1.5}, 
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee":24}, "cost": 2.5},
        "cappuccino":{"ingredients":{"water":250, "milk":100,"coffee":24},"cost": 3.0}}

profit = 10
resources = {
    "water":500, "milk": 200, "coffee":100,
}

def resources_report(resources):
    print("현재 남은 재료 입니다. :")
    print(f"'물' : {resources['water']:}")
    print(f"'우유' : {resources['milk']:}")
    print(f"'커피' : {resources['coffee']:}")
    return resources

def select_drink():
    order = input("어떤 음료를 원하시나요?: [espresso/latte/cappuccino] :")
    if order == 'off':
        exit()
    elif order == 'report':
        resources_report(resources)
        exit()
    elif order == 'espresso':
        return 'espresso'
    elif order == 'cappuccino':
        return 'cappuccino'
    elif order == 'latte':
        return 'latte'

def able_order(drink_name, resources):
    coffee = str(drink_name)
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print("물이 부족합니다.")
        exit()
        return False      
    elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
        print("우유가 부족합니다.")
        exit()
        return False
    elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print("원두가 부족합니다.")
        exit()
        return False
    elif MENU[coffee]["ingredients"]["water"] <= resources["water"] and MENU[coffee]["ingredients"]["milk"] <= resources["milk"] and MENU[coffee]["ingredients"]["water"] <= resources["water"]:
        print("음료 제작을 시작합니다. ")
        return True

def coin(drink_name, profit):
    coins = {"quarters": 0.25, "dimes":0.10, "nickels":0.05, 'pennies':0.01}
    cal = 0
    count_quarters = int(input("쿼터 동전을 넣어주세요. :"))
    cal = cal + coins["quarters"] * count_quarters
    count_dimes = int(input("다임 동전을 넣어주세요. :"))
    cal = cal + coins["dimes"] * count_dimes
    count_nickels = int(input("니켈 동전을 넣어주세요. :"))
    cal = cal + coins["nickels"] * count_nickels
    count_pennies = int(input("페니 동전을 넣어주세요. :"))
    cal = cal + coins["pennies"] * count_pennies
    print(type(cal),cal)
    print(f"총 {cal:.2f}$ 받았습니다. ")
    if cal < MENU[drink_name]['cost']:
        print("금액이 모자랍니다. 돈이 환불되었습니다.")
        exit()
        return False
    elif cal - MENU[drink_name]['cost'] > profit:
        print("기기에 거스름돈이 없어 주문이 취소되었습니다. 죄송합니다")
        exit()
        return False
    elif cal >= MENU[drink_name]['cost']:
        print(f"주문하신 {drink_name}, {MENU[drink_name]['cost']:.2f}$ / 투입 금액 {cal:.2f} $ / 거스름돈 {cal - MENU[drink_name]['cost']:.2f}$.")
        return cal
            
def is_transaction_successful(cal, drink_name, profit):
    if cal >= MENU[drink_name]['cost']:
        exchange = cal - MENU[drink_name]['cost']
        print(f"결제 완료. 거스름돈 : {exchange:.2f} $ 입니다.")
        profit = profit - exchange
        return profit
    else :
        print("금액이 부족합니다 !")
        exit()
        return False

def make_coffee(drink_name, able, resources):
    if able == True:
        resources['water'] = (resources['water'] - MENU[drink_name]["ingredients"]['water'])
        resources['milk'] = (resources['milk'] - MENU[drink_name]["ingredients"]['milk'])
        resources['coffee'] = (resources['coffee'] - MENU[drink_name]["ingredients"]['coffee'])
        return resources
    else:
        exit()

while True:
    drink_name = select_drink()
    able = able_order(drink_name, resources)
    update_resources = make_coffee(drink_name, able, resources)
    resources = update_resources
    total_money = coin(drink_name, profit)
    earn = is_transaction_successful(total_money, drink_name, profit)
    profit = profit + earn
