def is_sorted(t):
    t1 = t[:]
    if t==sorted(t1):
        return True
    return False

is_sorted([1, 2, 2])

is_sorted(['b', 'a'])