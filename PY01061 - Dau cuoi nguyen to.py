def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    str1 = int(s[:3])
    str2 = int(s[-3:])
    if isPrime(str1) and isPrime(str2):
        return "YES"
    else:
        return "NO"
    
t = int(input())
while t > 0:
    n = input().strip()
    print(check(n))

    t -= 1