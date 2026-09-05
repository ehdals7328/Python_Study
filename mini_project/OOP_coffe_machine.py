class CoffeeMachine:
    def __init__(self): # 초기 설정
        self.menu = {'espresso':{"ingredients":{"water": 50, "coffee":18,},"cost":1.5}, 
                    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee":24}, "cost": 2.5},
                    "cappuccino":{"ingredients":{"water":250, "milk":100,"coffee":24},"cost": 3.0}}
        self.profit = 0
        self.resources = {"water":300, "milk": 200, "coffee":100,}
        self.coins = {"quarters": 0.25, "dimes":0.10, "nickels":0.05, 'pennies':0.01}
    
    def resources_report(self): # 리소스를 출력하는 함수
        print("현재 남은 재료 입니다. :")
        print(f"'물' : {self.resources['water']:}")
        print(f"'우유' : {self.resources['milk']:}")
        print(f"'커피' : {self.resources['coffee']:}")
        print(f"기기잔고 {self.profit:.2f} $")

    def select_drink(self): # 사용자로부터 음료를 입력받는 함수
        order = input("어떤 음료를 원하시나요?: [espresso/latte/cappuccino] :")
        order = order.strip() # 입력데이터 전처리
        order = order.lower()

        if order == 'off':
            exit()
        if order == 'report':
            self.resources_report()
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

    def is_resource_sufficient(self, drink_name): # 입력받은 음료의 재료가 부족한지 확인하는 함수
        drink_ingredients = self.menu[drink_name]['ingredients']
        for item, amount in drink_ingredients.items():
            if amount > self.resources.get(item, 0):
                print("재료가 부족합니다")
                return False
        print("제작을 시작합니다.")
        return True

    def process_coins(self): # 동전을 투입
        # coins = {"quarters": 0.25, "dimes":0.10, "nickels":0.05, 'pennies':0.01}
        cal = 0.0
        for coin_name, value in self.coins.items():
            add_cal = int(input(f"{coin_name}동전을 넣어 주세요."))
            cal = cal + value * add_cal
        return cal
    
    def is_transaction_successful(self, drink_name, cal): # 돈이 충분할때 거래를 하는 함수
        cost = self.menu[drink_name]['cost']
        if cal >= cost:
            exchange = cal - cost
            print(f"\n{'=' * 32}\n결제 완료.")
            if exchange > 0:
                print(f"거스름돈은 {exchange:.2f}$입니다.")

            print(f"여기 주문하신 {drink_name}이 나왔습니다. 즐기세요")
            return cost
        else: #돈이 모자랄때 
            print("금액이 모자랍니다. 돈이 환불되었습니다.")
            return False

    def make_coffee(self, drink_name): # resources 를 갱신하는 함수
            drink_ingredients = self.menu[drink_name]['ingredients']
            for item, amount in drink_ingredients.items():
                self.resources[item] -= amount

    def add_profit(self, profit):
        self.profit += profit

if __name__ == "__main__":

    machine1 = CoffeeMachine()

    while True:
        drink = machine1.select_drink()
        if not drink:
            continue

        if not machine1.is_resource_sufficient(drink):
            continue

        inserted_coin = machine1.process_coins()
        earn = machine1.is_transaction_successful(drink, inserted_coin)
        if earn:
            machine1.make_coffee(drink)
            machine1.add_profit(earn)