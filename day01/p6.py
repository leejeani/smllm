if __name__ == '__main__':
    setData = {1,2,3,4,4}
    print(setData, type(setData))
    setData.add(5)
    print(setData, type(setData))
    setData.remove(3)
    print(setData, type(setData))
    setData2 = {5,2,3,6}
    setDat3 = setData.intersection(setData2)
    print(setDat3)
    setDat4 = setData.union(setData2)
    print(setDat4)
    setDat5 = setData.difference(setData2)
    print(setDat5)

    list1 = list(setDat5)
    print(list1, type(list1))
