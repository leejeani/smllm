g = 10
def myFunc(a, b, c=10):
    result = a + b + c
    global g
    g = a
    return result
def myFunc2(*args, **kwargs):
    result = 0
    result2 = 0
    for i in args:
        result = result + i
        global  g
        g = g + i
    for key, value in kwargs.items():
        result2 = result2 + value
    return [result,result2]

if __name__ == '__main__':
    a = 10
    b = 20
    result = myFunc(a=1, b=3, c=10)
    print(result)

    result2 = myFunc2(1,2,3,4,5, a=10, b=20, c=30)
    print(result2)
    print(result2[0])

    print(g)



