from collections import deque

MENU = """\n[1.곡 추가] [2.다음 곡] [3.이전 곡] [4.맨 앞에 넣기] [5.대기열 회전] [6.현재 상태] [0.종료]\n"""
queue = deque(['f', 'g', 'h', 'i', 'j']) # Queue
history = ['a', 'b', 'c', 'd', 'e'] # Stack
now = None # 현재곡

def show_status(now):
    print("=" * 44)
    print(f"{'MY PLAYLIST':^44}")
    print("=" * 44)
    print(f"{'Now Playing . . .':<} {now if now is not None else '(없음)'}")
    print("-" * 44)
    print(f"{'대기열':<} {len(queue)}곡 (먼저 넣은 곡부터 재생)")
    if len(queue) == 0:
        print(f"{('비어있음'):^35}")
    else:
        for i, song in enumerate(queue,1):
            print(f"{i}.{song}")
    print("-" * 44)
    print(f"{'재생 이력':<} {len(history)}곡 (최근에 들은 곡부터)")
    if len(history) == 0:
        print(f"{('비어있음'):^35}")
    else:
        for i, prev in enumerate(reversed(history),1):
            print(f"{i}.{prev}")
    print("=" * 44)

def add_song(title):
    queue.append(title)
    print(f"'{title}'을(를) 대기열 맨 뒤에 추가했습니다. 총 {len(queue)}곡")

def play_next(now):
    if len(queue) == 0:
        print("현재 대기열이 비어있습니다.")
        return now
    elif now is not None:
        history.append(now)
    now = queue.popleft()
    print(f"재생 {now}")
    return now

def play_prev(now):
    if len(history) == 0:
        print("재생 이력이 없습니다")
        return now
    else:
        if now is not None:
            queue.appendleft(now)
        now = history.pop()
        print(f"이전 곡 재생 {now}")
        return now

def add_urgent(title):
    queue.appendleft(title)
    print(f"{title}을(를) 대기열 맨 앞에 넣었습니다. (총 {len(queue)}곡)") 

def rotate_queue(n):
    if len(queue) == 0:
        print("대기열이 비어 있습니다.")
        return False
    else:
        queue.rotate(n)
        print(f"대기열을 {n}칸 회전했습니다.")
        print(f"{list(queue)}")

while True:
    print(MENU)
    select = int(input("번호를 입력하세요: "))
    if select == 1:
        add_name = input("추가할 곡 제목 :").strip()
        add_song(add_name)
        continue
    elif select == 2:
        now = play_next(now)
        continue
    elif select == 3:
        now = play_prev(now)
        continue
    elif select == 4:
        urgent = input("맨 앞에 넣을 음악 제목: ").strip()
        add_urgent(urgent)
        continue
    elif select == 5:
        rotate = int(input("대기열을 회전 할 칸수를 입력 :"))
        rotate_queue(rotate)
        continue
    elif select == 6:
        show_status(now)
        continue
    elif select == 0:
        print("종료합니다.")
        exit()
    else:
        print("다시 입력해 주세요: ")
        continue