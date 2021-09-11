N = int(input())
S = input()

if S[0] != S[N-1]:
    print(1)
    exit()
else:
    if len(S) == 3:
        print(-1)
        exit()


for i in range(N-1):
    if S[i] != S[N-1] and S[i+1] != S[N-1]:
        print(2)
        exit()

print(-1)



