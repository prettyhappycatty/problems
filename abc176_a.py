N, X, T = map(int, input().split())

times = N // X 
if N % X == 0:
    print(times*T)
else:
    print((times+1)*T)
