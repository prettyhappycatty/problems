N, A, B = map(int, input().split())
import math
    
if A > B:
    print(0)
elif N == 1 and A == B:
    if N == 1:
        print(1)
    else:
        print(0)
elif N == 1 and A != B:
    print(0)
else:
    print((B-A)*(N-2) + 1)