A, B, C = map(int, input().split())

if (A == B and C != B) or (A == C and B != C) or (C == B and C != A):
    print("Yes")
else:
    print("No")