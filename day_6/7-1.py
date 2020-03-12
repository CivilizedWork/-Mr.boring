import math
from prettytable import PrettyTable
def mysqrt(a):
    x = a
    y = 0
    while True:
        y = (x + a / x) / 2.0
        if abs(y - x) < 0.00001:
            break
        x = y
    return y


def test_squre_root():

    times=int(input('the times you want to test:'))
    print('a','      ','mysqrt(a)','        ',' math.sqrt(a)','       diff')
    for i in range(times):
        a = int(input())
        print(a,'      ',mysqrt(a),' ',math.sqrt(a),abs(math.sqrt(a)-mysqrt(a)))

test_squre_root()