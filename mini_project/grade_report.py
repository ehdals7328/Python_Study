SUBJECT = ('국어', '영어' , '수학')
names = ['가영', '다영', '아영']
scores = [90, 50, 70] #테스트의 편의를 위해 90점으로 설정

print(f"과목:{SUBJECT}")
print(f"등록된 학생: {len(names)}")
print(f"첫번째 학생: {names[0]}/{scores[0]}점")
print(f"마지막 학생: {names[-1]}/{scores[-1]}점")

add_student = input("추가할 학생 이름: ")
add_score = int(input("점수: "))

names.append(add_student)
scores.append(add_score)

print(names)
print(scores)
print(f"이제 {len(names)}명 입니다.")

total = sum(scores)
average = total / len(scores)
high = max(scores)
low = min(scores)

print(f"총점 : {total}")
print(f"평균 : {average:.1f}")
print(f"최고점 : {high}")
print(f"최저점 : {low}")

first = scores.index(high)
first_name = names[first]
spec_student = names.index('다영') # 다영만을 위한 코드
spec_score = scores[spec_student]

sorted_name = sorted(names)
sorted_score = sorted(scores, reverse=True)

#print(f"1등: {first_name} - scores[{first}]자리") 확인용 이므로 출력제외
print(f"다영의 점수: {spec_score}점 (name[{scores.index(spec_score)}])")
print(f"점수 내림차순: {sorted_score}")
print(f"이름 가나다순: {sorted_name}")

print(f"{'=' * 30}")
print(f"{'성 적 리 포 트':^30}")
print(f"{'=' * 30}")
print(f"{'이름':<12} {'점수':>8}")
print(f"{'-' * 30}")
print(f"{names[0]:<12} {scores[0]:>8}")
print(f"{names[1]:<12} {scores[1]:>8}")
print(f"{names[2]:<12} {scores[2]:>8}")
print(f"{names[3]:<12} {scores[3]:>8}")
print(f"{'-' * 30}")
print(f"{'평균':<12} {average:>8}")
print(f"{'1등':<12} {first_name:>8}")
print(f"{'=' * 30}")

out_index = scores.index(min(scores))
out_student = names[out_index]
low_student_name = names.pop(out_index)
low_student_score = scores.pop(out_index)
print(f"{low_student_name}학생은 최저점{low_student_score} 점이므로 탈락 입니다.")

names.insert(0,'한지민')
scores.insert(0,100)

sorted_name = sorted(names)
s_score = sorted(scores, reverse=True)
sorted_score = s_score.reverse()

total = sum(scores) # 한지민 이라는 학생이 추가되었으므로 총점, 평균, 최고점, 최저점을 다시 계산해야함
average = total / len(scores)
high = max(scores)
low = min(scores)

print(f"{'=' * 30}")
print(f"{'성 적 리 포 트':^30}")
print(f"{'=' * 30}")
print(f"{'이름':<12} {'점수':>8}")
print(f"{'-' * 30}")
print(f"{names[0]:<12} {scores[0]:>8}")
print(f"{names[1]:<12} {scores[1]:>8}")
print(f"{names[2]:<12} {scores[2]:>8}")
print(f"{names[3]:<12} {scores[3]:>8}")
print(f"{'-' * 30}")
print(f"{'평균':<12} {average:>8}")
print(f"{'1등':<12} {first_name:>8}")
print(f"{'=' * 30}")

scores.count(100)
print(f"100점 만점자는 {scores.count(100)}명 입니다. 축하드립니다.")