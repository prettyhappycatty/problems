N = int(input())

i = N
S = []

while i >0:
    if i % 2 == 1:#奇数なら
        S.append("A")
        i = i -1
    else:#偶数なら
        S.append("B")
        i = i // 2

#print(S)
ans = ""
for j in range(len(S)-1, -1, -1):
    ans = ans + S[j]

print(ans)
