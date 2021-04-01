N, A, B = list(map(int, input().split()))

def wa(x):
    s = str(x)
    cnt = 0
    for i in range(len(s)):
        cnt += int(s[i])
    return cnt


cnt = 0
for i in range(N+1):
    w = wa(i)
    #print(w)
    if w >= A and w <= B:
        cnt += i

print(cnt)
