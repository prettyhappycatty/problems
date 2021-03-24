A = int(input())
B = int(input())
C = int(input())
X = int(input())

aryA = [500*i for i in range(A+1)]
aryB = [100*i for i in range(B+1)]
aryC = [50*i for i in range(C+1)]
#print(aryA, aryB, aryC)

cnt = 0
for a in aryA:
    for b in aryB:
        for c in aryC:
            if a+b+c == X:
                cnt += 1
print(cnt)