with open("txt.txt", "w", encoding="UTF-8") as f:
    for i in range(1,11):
        f.write(f"{i}번째 문장 입니다. \n")
    print(f.read)