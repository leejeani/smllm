if __name__ == '__main__':
    list1 = [1,2,3,5,4]
    list1.sort()
    print(list1)
    list1.reverse()
    print(list1)
    list2 = sorted(list1)
    print(list2)

    list1.extend(list2)
    print(list1)






