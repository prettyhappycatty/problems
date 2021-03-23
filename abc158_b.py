N, A, B = map(int, input().split())

cnt = N // (A+B)
rest = N - cnt*(A+B)
#print(cnt, rest)
if rest >= A:
    blue = (cnt+1)*A
else:
    blue = cnt*A + rest
print(blue)