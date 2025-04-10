def lamtron(n):
    k = 1
    while n // 10 != 0:
        a = n % 10
        k = k * 10
        n = n // 10
        if a >= 5:
            n = n + 1
    return n * k

t = int(input())
while t :
    num = int(input())
    if(num < 10):
        print(num)
    else:
        print(lamtron(num))
    t = t - 1

    