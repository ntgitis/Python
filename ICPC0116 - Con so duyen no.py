def check(n):
    if(n[0] == n[len(n)-1]): return "YES"
    else: return "NO"

t = int(input())
while t:
    n = input()
    print(check(n))

    t -= 1