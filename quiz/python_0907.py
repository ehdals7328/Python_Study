# 사칙연산 Class 실습 

class FourCalStep1():
    pass

class FourCalStep2():
    def setdata(self, first, second):
        self.first = first
        self.second = second

class FourCalStep3():

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def __init__(self, first, second):
        self.first = first
        self.second = second


if __name__ == "__main__":

    a = FourCalStep1()
    print(f"빈 class도 객체를 만들 수 있음을 확인 {type(a)}")

    a = FourCalStep2()
    b = FourCalStep2()
    a.setdata(4, 2)
    b.setdata(3, 7)
    print(f"a.first,b.first : {a.first}, {b.first}")
    print(f"id(a), id(b) : {id(a)}, {id(b)}")
    print("힙의 서로 다른 자리를 가짐 , 인스턴스가 새로 만들어짐")

    a = FourCalStep3()
    b = FourCalStep3()
    a.setdata(4, 2)
    b.setdata(3, 7)
    print(f"3단계 사칙연산 add {a.add()} sub {a.sub()}, mul {a.mul()}, div {a.div()}")

    try:
        FourCalStep3().add()

    except AttributeError as e:
        print("3단계 오류 {e}")

    a = FourCal(4, 2)
    b = FourCal(3, 8)
    print(f"4단계 사칙연산 add {a.add()} sub {a.sub()}, mul {a.mul()}, div {a.div()}")
    print(f"4단계 사칙연산 add {b.add()} sub {b.sub()}, mul {b.mul()}, div {b.div()}")

    try:
        FourCal()
    except TypeError as e:
        print(f"4단계 오류 {e}")

    try:
        FourCal(4, 0).div()
    except ZeroDivisionError as e:
        print(f"나누기 오류 {e}")