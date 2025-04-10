def check(n):
    s = str(n)
    a, b = s[0], s[1]
    if len(s) < 2 : return "YES"
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            return "NO"
    return "YES"

t = int(input())
while t:
    n = int(input())
    print(check(n))

    t -= 1