fin=open('words.txt')
t = dict()
for line in fin:
    word=line.strip()
    t[word]=1
if 'apple' in t:
    print('Yes')