student = {'name':'김민준', 'age':20, 'major':'컴퓨터공학'}

student['email'] = 'minjun@example.com'
student['age'] = 21
student['hobbies'] = ['python','game']
del student['major']

#print(student['name'], student['age'], student['major'], student['email'], student['hobbies'])
print(student)
print(f"학생수 : {len(student)}개 항목")

print(student.get('name'))
print(student.get('phone'))

#student['phone'] = ['미등록']
print('email' in student, 'major' in student)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

print('=' * 34)
print(f"{' P R O F I L E ':^30}")
print('=' * 34)
print(f"{'이름':<12} {student['name']:>18}")
print(f"{'나이':<12} {student['age']:>18}")
print(f"{'이메일':<12} {student['email']:>18}")
print(f"{'전화':<12} {str(student.get('phone')):>18}")
print('-' * 34)
print(f"{'취미':<12} {str(student['hobbies']):>18}")
print(f"{'항목수':<12} {len(student):>18}")