N = int(input())
S = input()

for i in range(N):
    if S[i] == '1':
        if i % 2 == 1:
            print("Aoki")
        else:
            print("Takahashi")
        exit()

