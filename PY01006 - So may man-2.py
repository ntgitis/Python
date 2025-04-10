def check(num):
    for i in num:
        if(i != "4" and i != "7"):
            return "NO"
    return "YES"
        
t = int(input())
while t :
    num = input()
    print(check(num))
    t -= 1