python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민',]

python_set = set(python_list)
web_set = set(web_list)

print(f"파이썬 신청{len(python_list)}건 -> 실제 {len(python_set)}명")
print(f"웹개발{len(web_list)}건 -> 실제 {len(web_set)}명")

print(f"{sorted(python_set)}")
print(f"{sorted(web_set)}")

both = python_set & web_set
all_student = python_set | web_set
only_py = python_set - web_set
only_web = web_set - python_set
one_only = python_set ^ web_set

print(f"둘 다 수강 : {sorted(list(both))}")
print(f"전체 수강생 : {sorted(list(all_student))}")
print(f"파이썬만 : {sorted(list(only_py))}")
print(f"웹개발만 : {sorted(list(only_web))}")
print(f"한과목만 : {sorted(list(one_only))}")

name = '이서연'

print(f"{name} 파이썬 수강? {name in python_list}")
print(f"{name} 웹개발 수강? {name in web_list}")
print(f"{name} 둘다 수강? {name in both}")
print(f"{name} 하나라도 수강? {name in all_student}")
print(f"{name} 미수강? {name in one_only}")
print(f"{name} 교집합이 비었나? {name not in both}")

report = {'python':len(python_set), 'web':len(web_set), 'both':len(both), 'total':len(all_student)}
percent = report['both'] / report['total'] * 100
print(percent)
print(report)
print("=" * 32)
print(f"{'수 강 현 황':^30}")
print("=" * 32)
print(f"파이썬 {report['python']}명")
print(f"웹개발 {report['web']}명")
print("-" * 32)
print(f"둘 다 수강 {report['both']}명")
print(f"전체 인원 {report['total']}명")
print("=" * 32)
print(f"중복 수강률: {percent:.1f}%")