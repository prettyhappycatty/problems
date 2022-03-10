N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

set_t = set(T)

#print(set_t)

for i in range(len(S)):
    if S[i] in set_t:
        print("Yes")
    else:
        print("No")

