def rotate_word(str,n):
    for letter in str:
        if letter.isupper():
            start = ord('A')
        elif letter.islower():
            start = ord('a')
        else:
            return letter
        c = ord(letter) - start
        i = (c + n) % 26 + start

        print(chr(i),end='')
    print('')

rotate_word('melon',-10)

rotate_word('cheer',7)