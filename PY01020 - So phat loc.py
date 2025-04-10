def check(n):
    if (n[-2:] == "86"):
        return "YES"
    else:
        return "NO"
    
t = int(input())
while t:
    n = input()
    print(check(n))
    t -= 1