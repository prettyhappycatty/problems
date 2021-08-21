n = int(input())

A = list(map(int, input().split()))

ar1 = {}
ar2 = {}

for i in range(n):
    if i % 2 == 0:
        if A[i] not in ar1.keys():
            ar1[A[i]] = 0
        ar1[A[i]] += 1
    else:
        if A[i] not in ar2.keys():
            ar2[A[i]] = 0
        ar2[A[i]] += 1

ar1_sorted = sorted(ar1.items(), key=lambda x:x[1], reverse=True)
ar2_sorted = sorted(ar2.items(), key=lambda x:x[1], reverse=True)

if len(ar1_sorted) == 1 and  len(ar2_sorted) == 1 and ar1_sorted[0][0] ==  ar2_sorted[0][0]:
    #1種類で、数字が同じ
    print(ar1_sorted[0][1])
elif ar1_sorted[0][0] == ar2_sorted[0][0]:
    if len(ar1_sorted) == 1 or  len(ar2_sorted) == 1:
        print(n//2)
    else:
        a = (n//2-ar1_sorted[0][1]) + (n//2-ar2_sorted[1][1])
        b = (n//2-ar2_sorted[0][1]) + (n//2-ar1_sorted[1][1])
        print(min(a,b))
else: #一番多い数字が同じでないとき
    cnt = (n//2 - ar1_sorted[0][1]) + (n//2-ar2_sorted[0][1])
    print(cnt)
