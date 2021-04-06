N = int(input())
a = list(map(int, input().split()))

cnt = 1
cnt_break = 0
for i in range(len(a)):
    if cnt == a[i]:
        cnt += 1
    else:
        cnt_break += 1

if cnt_break == len(a):
    print(-1)
else:
    print(cnt_break)