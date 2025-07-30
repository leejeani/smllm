if __name__ == '__main__':
    name = input("Input Name")
    print(name)
    addr = input("Input Addr")
    print(addr)


    print(name, end=",")
    print(addr)
    print(name, addr, sep="---")

    num = int(input("Input Num"))
    print(num)
    nums = list(map(int, input("Input Nums").split()))
    print(nums)




