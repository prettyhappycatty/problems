S = input()

cnt = 0
for i in range(len(S)):
    cnt += int(S[i])

if cnt % 9 == 0:
    print("Yes")
else:
    print("No")