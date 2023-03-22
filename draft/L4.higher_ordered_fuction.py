def make_adder(n):
    def adder(k):
        return k*k+n
    return adder

a, b= 2, 1
print(make_adder(a)(b))