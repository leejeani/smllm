if __name__ == '__main__':
    a = input("값을 입력 하세요")
    a = int(a)
    if a > 3:
        print("OK")
    # if else
    if a > 10:
        print("High")
    else:
        print("Low")

    if a < 4:
        print("Low")
    elif a < 5:
        print("Medium")
    elif a < 10:
        print("High")
    else:
        print("input Again")

