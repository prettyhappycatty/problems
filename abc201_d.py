H, W= map(int, input().split())

A = []

aoki = 0
takahashi = 0
for i in range(H):
    tmp_A= input()
    A.append(tmp_A)
    for j in range(len(tmp_A)):
        if i == 0 and j == 0:
            continue
        if (i+j) % 2 == 1 and tmp_A[j] == "+":
            takahashi += 1
        elif (i+j) % 2 == 1 and tmp_A[j] == "-":
            takahashi += -1
        
        if (i+j) % 2 == 0 and tmp_A[j] == "+":
            aoki += 1
        elif (i+j) % 2 == 0 and tmp_A[j] == "-":
            aoki += -1

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")