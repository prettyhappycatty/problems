from wsgiref.handlers import IISCGIHandler


N = int(input())
A = list(map(int, input().split()))

S = []
ssum = 0

for i in range(len(A)):
    ssum += A[i]
    S.append(ssum % 360)
S.append(0)
S.append(360)
S.sort()
#print(S)

max_slice = 0
for i in range(len(S)-1):
    max_slice = max(max_slice, S[i+1]-S[i])

print(max_slice)



