N, Q = map(int, input().split())
S = input()


cnt = [0]
bef = S[0]
cnt_ac = 0
for i in range(1,len(S)):
    if bef == "A" and S[i] == "C":
        cnt_ac += 1
    cnt.append(cnt_ac)
    bef = S[i]

#print(cnt)

for i in range(Q):
    l, r = map(int, input().split())
    print(cnt[r-1]-cnt[l-1])


