N = int(input())

bef = False
cnt_max = 1
cnt = 0
for i in range(N):
    D1, D2 = map(int, input().split())
    #print(D1,D2)
    if D1 == D2:
        if bef == False:
            cnt = 1
        else:
            cnt += 1
            cnt_max = max(cnt_max, cnt)
        bef = True
    else:
        cnt_max = max(cnt_max, cnt)
        cnt = 0
#print(cnt_max)
if cnt_max >= 3:
    print("Yes")
else:
    print("No")
