def counter(word):
    count = 0
    for letter in word:
        if letter =='a':
            count+=1
    print(count)

counter('banana')
