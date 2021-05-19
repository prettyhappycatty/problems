a, b = map(int, input().split())
c, d = map(int, input().split())
dif1 = c - a
dif2 = d - b

if (dif1, dif2) == (0, 0):
    ans = 0
elif dif1 == dif2 or dif1 == -dif2: 
    ans = 1
elif abs(dif1) + abs(dif2) <= 3:
    ans = 1
elif (a+b+c+d) % 2 == 0:
    ans = 2
elif abs(dif1) + abs(dif2) <= 6:
    ans = 2
elif abs(dif1+ dif2) <= 3 or abs(dif1 - dif2) <= 3:
    ans = 2
else:
    ans = 3
print(ans)