seconds = 3725

hour = seconds // 3600
min = seconds % 3600 // 60
sec = seconds % 3600 % 60

print(f"{hour}시간 {min}분 {sec}초")
