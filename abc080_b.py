N = int(input())

S = str(N)

cnt = 0
for i in range(len(S)):
    si = S[i]
    cnt += int(si)

if N % cnt == 0:
    print("Yes")
else:
    print("No")