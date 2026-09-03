import sys

FILE_PATH ="C:/python_programming/Python_Study/mini_project/money/records.txt"
CATEGORIES = ["식비","교통","문화","기타"]


def add_record(date, category, item, amount):
    with open(FILE_PATH, 'a', encoding = 'utf-8')as f:
        f.write(f"{date},{category},{item},{amount}\n")
        print(f"기록했습니다. {date}, {category}, {item}, {amount}")

#add_record("2026-08-24", "식비", "점심 김밥", "7000")

def load_records():
    with open(FILE_PATH, 'a', encoding = 'utf-8'):
        pass
    with open(FILE_PATH, 'r', encoding = 'utf-8')as f:
        list_line = []
        for line in f:
            line.replace('\n','')
            split_line = line.split(",")
            date = split_line[0]
            category = split_line[1]
            item = split_line[2]
            amount = split_line[3]
            line = {f"date":date, "category":category, "item":item, "amount":int(amount),}
            list_line.append(line)

    return list_line

def show_all():
    r = load_records()
    sum = 0
    print("=" * 46)
    print(f"{'용 돈 기 록 장':^35}")
    print("=" * 46)
    print(f"{'번호':<5}{'날짜':<10}{'분류':<7}{'내용':<8}{'금액':>9}")
    print("-" * 46)
    for i in range(len(r)):
        print(f"{i+1:<5} {r[i]['date']:<12} {r[i]['category']:<7} {r[i]['item']:<8} {r[i]['amount']:>9,}")
        sum = sum + r[i]['amount']
    print("-" * 46)
    print(f"{'합계':<5} {sum:^35}")
    print("=" * 46)

def summary():
    r_summary = load_records()
    summary = {}
    if r_summary == False:
        print("기록이 없습니다. ")
        return False
    else:
        for line in r_summary:
            if '식비' in line:
                summary['식비'] = line['amount']
            elif '교통' in line:
                summary['교통'] = line['amount']
            elif '문화' in line:     
                summary['문화'] = line['amount']
        print(summary)
summary()