def avoid(word,forbidden):
    cnt=0
    for letter in word:
        if letter in forbidden:
            cnt=cnt+1
    return cnt



fbd=input('Input a forbidden letter')
print(avoid('interrupt',fbd))