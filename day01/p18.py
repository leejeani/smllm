import pickle

if __name__ == '__main__':
    num = input("Input num")
    try:
        num = num + 100
    except TypeError:
        print("다시 입력 하세요")

    print(num)



