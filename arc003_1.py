N = int(input())
S = input()

cnt = 0
for i in range(len(S)):
    if S[i] == "A":
        cnt += 4
    elif S[i] == "B":
        cnt += 3
    elif S[i] == "C":
        cnt += 2
    elif S[i] == "D":
        cnt += 1

print(cnt/len(S))

