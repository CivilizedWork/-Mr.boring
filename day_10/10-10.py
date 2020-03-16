import bisect
def in_bisect(t,n):
    s=t[:]
    s.sort()
    index=bisect.bisect_left(s,n)
    return index

t=[1,5,4,3]
print(in_bisect(t,3))