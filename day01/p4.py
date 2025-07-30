if __name__ == '__main__':
    dic1 = {"a":1, "b":2, "c":3}
    print(dic1["a"])
    dic1Key = dic1.keys()
    print(dic1Key, type(dic1Key))
    dic1Value = dic1.values()
    for i in dic1Value:
        print(i)

    print(dic1Value, type(dic1Value))
    dic1Items = dic1.items()
    print(dic1Items, type(dic1Items))
    print(dic1.popitem())



