def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    res = sum(int(i) for i in str(n))
    print("YES" if isPrime(res) else "NO")
    t -= 1