from mypackae.p13 import myFunc as m
import mypackae.Calculator as cal

if __name__ == '__main__':
    result = m(1,2,3)
    print(result)
    cal1 = cal.Calculator(10,20)
    result1 = cal1.add()
    print(result1)