python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민',]

line = '=' * 32
line_2 = '-' * 32
#리스트를 집합으로 캐스팅
python_set = set(python_list)
web_set = set(web_list)

# 집합 연산
both = python_set & web_set
all_student = python_set | web_set
only_py = python_set - web_set
only_web = web_set - python_set
one_only = python_set ^ web_set

report = {'python':len(python_set), 'web':len(web_set), 'both':len(both), 'total':len(all_student), 'only_py':len(only_py), 'only_web':len(only_web)} # 집합 연산 결과 (단위 : 인원수)
percent = report['both'] / report['total'] * 100 # 중복 수강률 확인

print(f"중복 검사를 실시 합니다. \n파이썬 신청{len(python_list)}건 -> 실제 {len(python_set)}명")
print(f"웹개발{len(web_list)}건 -> 실제 {len(web_set)}명")

def student_check(name):
    print(f"{name} 파이썬 수강? {name in python_list}")
    print(f"{name} 웹개발 수강? {name in web_list}")
    print(f"{name} 둘다 수강? {name in both}")
    print(f"{name} 하나라도 수강? {name in all_student}")
    print(f"{name} 미수강? {name in one_only}")
    print(f"{name} 교집합이 비었나? {name not in both}")

def print_list():
    print(report)
    print(line)
    print(f"{'수 강 현 황':^30}")
    print(line)
    print(f"파이썬 {report['python']}명")
    print(f"파이썬만 {report['only_py']}명")
    print(f"웹개발 {report['web']}명")
    print(f"웹개발만 {report['only_web']}명")
    print(line_2)
    print(f"둘 다 수강 {report['both']}명")
    print(f"전체 인원 {report['total']}명")
    print(line)
    print(f"중복 수강률: {percent:.1f}%")

name = input("수강내역을 확인할 학생 이름을 입력해 주세요. :")
student_check(name)
print_list()