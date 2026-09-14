# 1. 이터러블(리스트) 정의
my_list = [10, 20, 30]

# 2. 이터러블을 이터레이터로 변환
my_iter = iter(my_list)

print(type(my_iter)) # <class 'list_iterator'>

# 3.next() 를 이용해 값을 하나씩 꺼냄
print(next(my_iter)) # 10 출력
print(next(my_iter)) # 20 출력
print(next(my_iter)) # 30 출력

# 4. 데이터가 더 이상 없는데 호출하면 예외 발샐
try:
    print(next(my_iter))
except StopIteration:
    print("데이터 소진: 반복 종료")