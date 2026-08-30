email = "hong.gildong@example.com"

find = email.find('@')
pos = int(find)

e_split = email.split('@')
remove_com = e_split[1][:-4]
print(pos)
print(e_split)
print(e_split[0].upper(), remove_com)

# split이 더 간단해 보임.