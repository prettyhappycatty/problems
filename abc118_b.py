N, M = list(map(int, input().split()))
cnt_dict = {}
for i in range(M):
    cnt_dict[i] = 0

for i in range(N):
    tmp = list(map(int, input().split()))
#    print(tmp)
    for j in range(1, tmp[0]+1):
        cnt_dict[tmp[j]-1] += 1

#print(cnt_dict)

cnt = 0
for i in range(M):
    if cnt_dict[i] == N:
        cnt += 1

print(cnt)