def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(66,11))
print(gcd(66,12))