#a
N = int(input())
X = [int(x) for x in input().split()]

X.sort()

divsum = 0
for i in range(len(X)):
    if i == 0:
        divsum = X[i]
        continue
    divsum = (divsum + X[i])/2

print(divsum)