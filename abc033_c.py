S = input()
N = len(S)

newS = S.split('+')

cnt = 0
for s in newS:
    if "0" not in s:
        cnt += 1

print(cnt)