import math

a=int(input('请输入a:'))
b=int(input('请输入b:'))
c=int(input('请输入c:'))
n=int(input('请输入n:'))


def check_fermat(a,b,c,n):
    if n>2 and pow(a,n)+pow(b,n)==pow(c,n):
        print('Holy smokes,Fermat was wrong!')
    else:
        print("No,that doesn't work.")

check_fermat(a,b,c,n)


