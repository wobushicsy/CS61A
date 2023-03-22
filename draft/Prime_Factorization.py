def prime(n):
    i = 2
    while(i<=n):
        if(n%i!=0):
            i += 1
        else:
            print(i)
            n /= i
            i = 2

prime(858)