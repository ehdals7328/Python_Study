s = "  Life is too short, You need Python  " # 앞뒤에 공백이 두 칸

striped = s.strip()
count = striped.count('o')
find = striped.find('short')
no_find = striped.find('Java')
replace = striped.replace('Python','Java')
split = striped.split()

print(len(s), len(striped))
print(count)
print(find, no_find)
print(replace)
print(split)
print(len(split))
