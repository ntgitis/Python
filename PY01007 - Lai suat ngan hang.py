t = int(input())  
while t:  
    n, x, m = map(float, input().split())
    year = 0 
    while n < m:
        n += n*(x/100)
        year += 1
    print(year)
    t -= 1