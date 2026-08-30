a = "20260823Sunny"

year = a[0:4]
month = a[4:6]
date = a[6:8]
weather = a[8:]
reverse = a[::-1]

print(f"{year} {month} {date} {weather}\n{year}년 {month}월 {date}일의 날씨는 {weather}입니다.")
print(reverse)