import time
import threading

def download_file(file_name):
    print(f"[{file_name}] 다운로드 시작...")
    time.sleep(2)  # 다운로드에 2초 걸림 (I/O 대기)
    print(f"[{file_name}] 다운로드 완료!")

start = time.time()
print("Start")
# 파일 3개를 순서대로 다운로드
files = ["File-A", "File-B", "File-C"]
threads = []

for i in files:
    t = threading.Thread(target=download_file, args=(files[i],))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"전체 걸린 시간: {end - start:.2f}초")