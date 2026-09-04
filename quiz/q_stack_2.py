# Stack 실습, 괄호 검사 알고리즘

def check_brackets(text):
    stack = []

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True

print(check_brackets('(a + b)'))  
print(check_brackets('((a + b)'))  
print(check_brackets('a + b)')) 