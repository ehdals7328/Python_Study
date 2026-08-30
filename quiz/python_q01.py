a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b, a is c, a == c)
print(id(a) == id(b), id(a) == id(c))

b.append(4)
print(a)
