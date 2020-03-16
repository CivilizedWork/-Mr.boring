def is_anagram(a,b):
    count=0
    if len(a)==len(b):
        for i in a:
            if i in b:
                count=count+1
        if count == len(a):
            return True
    return False

is_anagram('banana','ban')


