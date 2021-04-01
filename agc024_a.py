A, B, C, K = list(map(int, input().split()))

#A kou 
#B chuu
#C tei

#奇数回の時にB-A
#偶数会の時にA-B

if abs(A-B) > 10**18:
    print('unfair')
else:
    if K % 2 == 1:
        print(B-A)
    else:
        print(A-B)