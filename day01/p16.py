if __name__ == '__main__':
    with open("data/mytext.txt", "w", encoding="utf-8") as f:
        print("오, 신기 하다.1", file=f)
        print("오, 신기 하다.2", file=f)
        print("오, 신기 하다.3", file=f)
        f.write("abc")
        f.close()
    with open("data/mytext.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print(data)
        f.close()
    with open("data/mytext.txt", "r", encoding="utf-8") as f:
        data = f.readline()
        print(data)
        f.close()
    with open("data/mytext.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        print(data[1])
        f.close()



