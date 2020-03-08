def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f,s):
    f(s)
    f(s)

do_twice(print_twice,'spam')