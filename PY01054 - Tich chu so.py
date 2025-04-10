def product(n):
    prod = 1
    check = False
    for i in str(n):
        if i != "0":
            prod *= i
            check = True

    return prod if check else 0

t = int(input())
while t > 0:
    n = input()
    print(product(n))

    t -= 1