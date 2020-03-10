import math
def check_fermat(a,b,c,n):
    if n>2 and pow(a,n)+pow(b,n)==pow(c,n):
        print('Holy smokes,Fermat was wrong!')
    else:
        print("No,that doesn't work.")