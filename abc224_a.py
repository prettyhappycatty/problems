S = input()
N = len(S)

if S[N-2:N] == "er":
    print("er") 
    exit()

if S[N-3:N] == "ist":
    print("ist") 
    exit()

