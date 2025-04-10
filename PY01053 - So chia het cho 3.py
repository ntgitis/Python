def check(n):
    if (n % 3 == 0):
        return "YES"
    else:
        return "NO"
    
t = int(input())
while t:
    n = int(input())
    print(check(n))

    t -= 1