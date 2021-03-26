A, B = list(map(int, input().split()))
S = input().split('-')

if A == len(S[0]) and B == len(S[1]):
    print('Yes')
else:
    print('No')