L, R = map(int, input().split())
S = input()


if L > 1:
    print(S[:L-1]+S[R-1:L-2:-1]+ S[R:])
else:
    print(S[R-1::-1]+ S[R:])

