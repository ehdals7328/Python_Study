import time
import multiprocessing

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working{i}")

if __name__ == "__main__":
    print("Start")
    start = time.time()

    processes = []

    for i in range(5):
        p = multiprocessing.Process(target = long_task)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("End")
    print(f"걸린 시간 {end-start:.2f}초")