
qwerty = "abcdefghijklmnopqrstuvwxyz"

P = list(map(int, input().split()))

ans = []
for i in range(len(P)):
    ans.append(qwerty[P[i]-1])

print("".join(ans))
