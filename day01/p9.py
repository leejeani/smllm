if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    for i in list1:
        print(i)

    result = [i*100 for i in list1]
    print(result)

    print('-----')
    i = 0
    while i < 5:
        print(list1[i])
        i = i + 1
