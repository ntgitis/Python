def swap_number(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)

t = int(input())
while t > 0:
    [p, q] = input().split()
    s = input().split()
    if len(s) == 2:
        a, b = s[0], s[1]
    else:
        a = s[0]
        b = input()

    x = swap_number(a, b, p, q)
    y = swap_number(a, b, q, p)     
    print(min(x, y), max(x, y))

    t -= 1