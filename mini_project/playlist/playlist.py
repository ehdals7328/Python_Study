from collections import deque

queue = deque(['f', 'g', 'h', 'i', 'j']) # Queue
history = ['a', 'b', 'c', 'd', 'e'] # Stack
now = '애국가' # 현재곡

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

