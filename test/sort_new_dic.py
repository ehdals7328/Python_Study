# 이 기능은 딕셔너리의 리스트를 카테고리별로 합산해주는 기능을 함.
records = [
    {"category": "식비", "amount": 10000},
    {"category": "교통", "amount": 2500},
    {"category": "식비", "amount": 8000},
    {"category": "문화", "amount": 15000}
]

def total_payment(records):
    total = {}
    for line in records:
        category = line["category"]
        amount = line["amount"]
        total[category] = total.get(category, 0) + amount
        
    return total

a = total_payment(records)
print(a)