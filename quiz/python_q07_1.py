email = "hong.gildong@example.com"

find = email.find('@')
pos = int(find)

front_sliced = email[:pos]
back_sliced = email[pos+1:]

u = front_sliced.upper()
l = back_sliced.lower()
l2 = l[:-4]

print(f"\nslice로 실행한 결과: \n{find}")
print(front_sliced, back_sliced)
print(u,l2)