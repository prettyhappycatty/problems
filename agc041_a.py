N, A, B = list(map(int, input().split()))

if (B-A)%2 == 0:
    ans =  (B - A)//2
else:
    ans = min(A-1, N-B) + (B - A + 1)//2

print(int(ans)) 