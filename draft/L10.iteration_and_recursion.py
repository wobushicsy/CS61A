def sum_iter(n):
    res = 0
    for i in range(n+1):
        res += i
    return res

def sum_recur(n):
    if n == 0:
        return 0
    else:
        return n + sum_recur(n-1)

print(sum_iter(5))
print(sum_recur(5))
