N, A, X, Y= map(int, input().split())

if A <= N:
    #A+1以降につえてはYえん
    print(A*X + (N-A)*Y)
else:
    print(X*N)