TMP = input().split()
a = int(TMP[0])
b = int(TMP[1])


if a > b:
    bigger = a
else:
    bigger = b

TMP = input().split()
c = int(TMP[0])
d = int(TMP[1])

if c > d:
    ans = bigger - d
else:
    ans = bigger - c

print(ans)