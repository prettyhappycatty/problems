S = input()

change_times = 0
N = len(S)

for i in range(N):
    if i > 0 and S[i] != S[i-1]:
        change_times += 1

print(change_times)
