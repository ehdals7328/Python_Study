import sys

FILE_PATH =r"C:\workspace\python_programming\Python_Study\mini_project\money\records.txt"
CATEGORIES = ["식비","교통","문화","기타"]


def add_record(date, category, item, amount):
    with open(FILE_PATH, 'a', encoding = 'utf-8')as f:
        f.write(f"{date},{category},{item},{amount}\n")
        print(f"기록했습니다. ({date}, {category}, {item}, {amount}원)")

def load_records():
    list_file = []
    with open(FILE_PATH, 'a', encoding = 'utf-8'):
        pass
    with open(FILE_PATH, 'r', encoding = 'utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            else:
                read_file = {}
                data, category, item, amount = line.split(",")
                amount = int(amount)
                read_file['data'] = data
                read_file['category'] = category
                read_file['item'] = item
                read_file['amount'] = amount
                list_file.append(read_file)
    return list_file            

def show_all():
    sum = 0
    records = load_records()
    print("=" * 46)
    print(f"{'용 돈 기 록 장':^35}")
    print("=" * 46)
    print(f"{'번호':<5}{'날짜':<10}{'분류':<7}{'내용':<8}{'금액':>9}")
    print("-" * 46)
    if len(records) == 0:
        print("아직 기록이 없습니다.")
        return False
    else:
        for i in range(len(records)):
            print(f"{i+1:<5} {records[i]['data']:<12} {records[i]['category']:<7} {records[i]['item']:<8} {records[i]['amount']:>9,}")
            sum = sum + records[i]['amount']
    print("-" * 46)
    print(f"{'합계':<5} {sum:^35}")
    print("=" * 46)

def summary():
    summary_records = load_records()
    total_sum = 0
    new_dic = {}
    if len(summary_records) == 0:
        print("기록이 없습니다")
        return False     
    for line in summary_records:
        if line['category'] in new_dic:
            new_dic[line['category']] += int(line['amount'])
        else:
            new_dic[line['category']] = int(line['amount'])
        total_sum += int(line['amount'])
    print("-"*34)
    print(f"{'분류별 지출':^25}")
    print("-"*34)
    sorted_records = sorted(new_dic, key=lambda k: new_dic[k], reverse=True)
    for i in range(len(new_dic)):
        print(f"{sorted_records[i]} {new_dic[sorted_records[i]]:,}원 {new_dic[sorted_records[i]]/total_sum * 100:.1f}%")
    print("-"*34)
    print(f"총 지출 {total_sum}원")
    print(f"기록 수 {len(summary_records)}건")
    print(f"평균 {int(total_sum/len(summary_records)):,}원")
    print("-"*34)
    return new_dic

def search(word):
    records = load_records()
    search_sum = 0
    found = [r for r in records if word in r['item'] or word in r['category']]
    print(f"{word} 검색 결과: {len(found)}건")
    if len(found) <= 0:
        print("검색 결과가 없습니다.")
        return False
    else:
        for i in range(len(found)):
            print(f"{i+1}. {found[i]['data']} {found[i]['category']} {found[i]['item']} {found[i]['amount']:,}")
            search_sum = search_sum + found[i]['amount']
    print(f"합 계{search_sum:,}원")

args = sys.argv[1:]

if len(args) > 0:
    command = args[0]

    if command == 'list':
        show_all()
    elif command == 'sum':
        summary()
    elif command == 'find' and len(args) < 1:
        word = args[1]
        search(word)
    else:
        print("사용법 : python money.py [list|sum|find 검색어] 입니다. ")
else:
    while True:
        print("\n1. 기록추가 2. 전체보기 3. 통계 4. 검색 0. 종료 ")
        select = input("번호를 선택하세요: ")

        if select == '1':
            date = input("날짜(예:2026-08-24): ")
            category = input(f"분류:{CATEGORIES}")
            if category not in CATEGORIES:
                print("존재하지 않는 분류 입니다. ")
                continue
            item = input("내용: ")
            amount = input("금액: ")
            add_record(date, category, item, amount)

        elif select == '2':
            show_all()
            continue

        elif select == '3':
            summary()

        elif select == '4':
            word = input("검색어를 입력해 주세요: ")
            search(word)

        elif select == '0':
            print("프로그램을 종료합니다. ")
            exit()

        else:
            print("없는 번호 입니다. ")
            continue