def eval_loop():
    while True:
        x=input('Input:')
        if x=='done':
            break
        else:
            print(eval(x))


eval_loop()