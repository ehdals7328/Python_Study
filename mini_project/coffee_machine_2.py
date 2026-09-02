SERVICES = {
    "city_tour": {"requirements": {"battery": 30, "time": 40}, "fare": 15000},
    "airport": {"requirements": {"battery": 60, "time": 80, "trunk_space": 2}, "fare": 40000},
    "short_trip": {"requirements": {"battery": 15, "time": 20}, "fare": 7000} 
}

company_profit = 0
fleet_resources = {
    "battery": 200,      # 메인 충전 허브의 가용 전력량 (kWh)
    "time": 300,         # 현재 투입 가능한 로보택시들의 총 영업 가능 시간 (분)
    "trunk_space": 5     # 현재 서비스 가능한 트렁크 공간 총량
}

def resources_report(fleet_resources, company_profit): # 리소스를 출력하는 함수
    print("현재 남은 리소스입니다:")
    print(f"'배터리' : {fleet_resources['battery']} kWh")
    print(f"'영업 가능 시간' : {fleet_resources['time']} 분")
    print(f"'트렁크 공간' : {fleet_resources['trunk_space']} 개")
    print(f"회사 수익: {company_profit} 원")
    return False

def select_service():
    selection = input("어떤 경로를 원하시나요? [city_tour/airport/short_trip]: ")
    selection = selection.strip().lower()

    if selection == 'off':
        exit()
    if selection == 'report':
        resources_report(fleet_resources, company_profit)
        return False
    if selection == 'city_tour':
        return 'city_tour'
    if selection == 'airport':
        return 'airport'
    if selection == 'short_trip':
        return 'short_trip'
    else:
        print("다시 입력해 주십시오.")
        return False

def is_fleet_ready(selection, resources): # 선택한 서비스의 리소스가 충분한지 확인하는 함수
    service = selection
    if SERVICES[service]['requirements']['battery'] > resources['battery']:
        print("배터리가 부족합니다.")
        return False      
    elif SERVICES[service]['requirements']['time'] > resources['time']:
        print("영업 가능 시간이 부족합니다.")
        return False
    elif SERVICES[service]['requirements'].get('trunk_space', 0) > resources.get('trunk_space', 0):
        print("트렁크 공간이 부족합니다.")
        return False
    else:
        print("리소스가 충분합니다. 서비스 시작을 준비합니다.")
        return True

def payment_process(selection, company_profit): # 결제 처리
    fare = SERVICES[selection]['fare']
    print(f"서비스 요금은 {fare} 원입니다.")
    payment = int(input("결제 금액을 입력해주세요: "))
    
    if payment < fare:
        print("금액이 모자랍니다. 결제가 취소되었습니다.")
        return False
    else:
        change = payment - fare
        if change > 0:
            print(f"거스름돈 {change} 원을 반환합니다.")
        return fare

def dispatch_vehicle(selection, resources): # 리소스를 갱신하는 함수
        resources['battery'] -= SERVICES[selection]['requirements']['battery']
        resources['time'] -= SERVICES[selection]['requirements']['time']
        resources['trunk_space'] -= SERVICES[selection]['requirements'].get('trunk_space', 0)
        return resources

while True:
    selection = select_service()
    if selection == False: # 다른 명령어 ex)Report or 오타 , 처음으로
        continue
    ready = is_fleet_ready(selection, fleet_resources) # 선택 받은 서비스의 리소스가 충분한지 확인
    if ready == False: # 리소스가 충분하지 않다면 처음으로
        continue
    earn = payment_process(selection, company_profit) # 결제 처리
    if earn == False: # 결제가 실패하면 처음으로
        continue
    company_profit += earn # 결제가 성공하면 회사 수익 갱신
    updated_resources = dispatch_vehicle(selection, fleet_resources) # 리소스를 갱신
    if updated_resources == False: # 리소스 갱신이 실패하면 처음으로
        continue
    fleet_resources = updated_resources
