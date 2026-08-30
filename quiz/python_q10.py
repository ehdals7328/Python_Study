apple = "사과"
banana = "바나나"
water = "수박"

name = "상품명"
count = "수량"
price = "단가"
cost = "금액"

print(f"{name:<10}{count:^8}{price:^8}{cost:>6}")
print('*' * 38)
print(f"{apple:<10} {3:^8}{1500:^8,}{4500:>6,}")
print(f"{banana:<10} {12:^8}{800:^8,}{9600:>6,}")
print(f"{water:<10} {1:^8}{22000:^8,}{22000:>6,}")
print('*' * 38)
print(f"{'합계':<10} {36100:^8,}")