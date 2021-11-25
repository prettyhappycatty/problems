S, T, X = map(int, input().split())

if S <= T:
    if S <= X and X < T:
        print("Yes")
    else:
        print("No") 
else:
    T = T + 24
    if X < S:
        X = X + 24
        
    if S <= X and X < T:
        print("Yes")
    else:
        print("No") 
