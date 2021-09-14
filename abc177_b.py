S = input()
T = input()

cnt_smallest = len(T)
for st in range(len(S)-len(T)+1):
    cnt = 0
    for i in range(len(T)):
        #print(S[st+i], T[i])
        if S[st+i] != T[i]:
            cnt += 1
    cnt_smallest = min(cnt_smallest, cnt)

print(cnt_smallest)



