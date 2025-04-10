def fibo(n, m):
    res = []
    f1, f2 = 1, 1
    for i in range(1, m+1):
        if i >= n:
            res.append(f1)
        f1, f2 = f2, f1 + f2
    return res

t = int(input())
while t > 0:
    a, b = map(int , input().split())
    res = fibo(a, b)
    print(*res)
    t -= 1


