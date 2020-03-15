def uses_all(word, required):
    cnt=0
    for letter in required:
        if letter not in word:
            return False
    cnt=cnt+1
    return cnt

fin = open('words.txt')
cnt=0
for line in fin:
    word=line.strip()
    cnt=cnt+uses_all(word,'aeiou')
print(cnt)