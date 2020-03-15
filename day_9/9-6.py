def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

fin=open('words.txt')
cnt=0
for line in fin:
    word=line.strip()
    if is_abecedarian(word):
        cnt=cnt+1
print(cnt)
