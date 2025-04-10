n = int(input())
a =[]

sum_up = 0
sum_down = 0

for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())
for i in range(n):
    for j in range(n):
        if i < j: sum_up += a[i][j]
        elif i > j: sum_down += a[i][j]

if abs(sum_up - sum_down) <= k:
    print(f"YES\n{abs(sum_up - sum_down)}")
else:
    print(f"NO\n{abs(sum_up - sum_down)}")