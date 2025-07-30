def myFunc(a, b, c=10):
    result = a + b + c
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