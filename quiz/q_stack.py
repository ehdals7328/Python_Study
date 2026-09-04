# Stack - 실습
# 입력한 텍스트를 역순으로 추출하는 프로그램 작성
# 입력은 'Python'

text = 'Python'
list_txt = list(text)
result = []

for _ in range(len(list_txt)):
    result.append(list_txt.pop())

a = ''.join(result)
print(a)