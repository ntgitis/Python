def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    snt = {"2", "3", "5", "7"}
    for i in range(len(n)):
        pos = isPrime(i)
        val = n[i] in snt
        if pos != val:
            return "NO"
    return "YES"

t = int(input())
while t > 0:
    n = input()
    print(check(n))

    t -= 1