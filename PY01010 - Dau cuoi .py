def check(str):
    if(str[:2] == str[-2:]):
        return "YES"
    else:
        return "NO"

t = int(input())
while t:
    str = input()
    print(check(str))
    t -= 1