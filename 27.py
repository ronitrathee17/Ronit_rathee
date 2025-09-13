for a in range(2, 101):
    prime=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            prime=False
            break
    if prime:
        print(a,end=' ')