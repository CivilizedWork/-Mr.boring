def do_four(f,s):
    do_twice(f, s)
    do_twice(f, s)


def do_twice(f,s):
    f(s)
    f(s)

do_four(print,'m')
