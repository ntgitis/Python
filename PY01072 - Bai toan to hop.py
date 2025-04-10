from itertools import combinations
def lietke(a, k):
    a = sorted(set(a))
    tohop = combinations(a, k)
    for comb in tohop:
        print(" ".join(map(str, comb)))

n, k = map(int, input().split())
a = list(map(int, input().split()))
lietke(a, k)