import time
def test1():
    fin = open('words.txt')
    t =[]
    for line in fin:
        word=line.strip()
        t.append(word)
    return t

def test2():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t

start_time = time.time()
t = test1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = test2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')
