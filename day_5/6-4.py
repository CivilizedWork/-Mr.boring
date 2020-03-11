def is_power(a,b):
    if a==1:
        return True
    elif a==0:
        return False
    if a%b==0:
        return is_power(a/b,b)
    return False
print(is_power(4,2))
print(is_power(4,3))


