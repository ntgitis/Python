def count(n, string):
    uniq = set(string)
    return len(uniq)

n = int(input())
string = [input().strip() for _ in range(n)]

print(count(n, string))