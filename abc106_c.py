S = input()
K = int(input())

target = '1'
for i in range(len(S)):
    #print(S[i], i, K)
    if i < K and S[i] != '1':
        target = S[i]
        break

print(target)