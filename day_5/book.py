def factorial(n):
    if n==0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse
        print(result)
        return result

t=factorial(3)
print(t)