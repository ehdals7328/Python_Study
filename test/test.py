# 짝수 검사기
def check(a):
    def wrapper(b):
        c = a % b
    return wrapper

couple = check(2)


print(couple(3))
