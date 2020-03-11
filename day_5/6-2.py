def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

print(ack(3,4))
#如果m，n值较大时，会超过递归的最大深度，从而无法运行