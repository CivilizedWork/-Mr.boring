def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#遍历，查看字符串里面是否有小写字符
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#错的，始终判断字母c 是不是小写
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
#将检测到的最后一个小写字符赋值给flag并返回flag
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
#遍历，如果不是小写就返回False，如果是小写就返回True