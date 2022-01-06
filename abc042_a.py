A, B, C = map(int, input().split())

dic = {5:0, 7:0}

if A == 5 or A == 7:
    dic[A] += 1
if B == 5 or B == 7:
    dic[B] += 1
if C == 5 or C == 7:
    dic[C] += 1

if dic[5] == 2 and dic[7] == 1:
    print("YES")
else:
    print("NO")
