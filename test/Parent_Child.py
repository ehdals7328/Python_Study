class Parent():
    def __init__(self):
        self.name = 'a'
        self.age = '1'
        self.color = 'red'


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = 'b'
        self.age = '2'


p = Parent()
c = Child()

print(p.name)
print(p.age)
print(p.color)

print(c.name)
print(c.age)
print(c.color)
