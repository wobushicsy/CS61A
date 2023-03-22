def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    len = 0
    while (n != 1):
        print(n)
        if(n % 2 == 0):
            len += 1
            n //= 2
        else:
            len += 1
            n = 3*n+1
    print(n)
    return len

a = hailstone(10)
print(a)