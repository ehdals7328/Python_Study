name = input("상품명을 입력해 주세요." )
price = int(input("단가를 입력해 주세요. "))
count = int(input("수량을 입력해 주세요. "))

tax = 0.1

def cost(x,y):
    cost = int(x * y)
    return cost

cost = cost(price,count)

print(cost)

print('=' * 35)
print(f"{'영수증':>15}")
print('=' * 35)
print(f"{name} {count:^3}개 {cost:>8,}원")
print('-' * 35)
print(f"부가세(10%) {int(cost * tax):>16,}원")
print(f"합계 {int(cost * (1 - tax)):>8,}원")
print('=' * 35)