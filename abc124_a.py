A, B = map(int, input().split())

if A-B > 0:
    print(A+(A-1))
elif B-A > 0:
    print(B+(B-1))
else:
    print(B+A)