S = input()

if S[0] == S[1] == S[2] == S[3]:
    print("Weak")
    exit()

if (int(S[0]) + 1)%10 == int(S[1]) and  (int(S[1]) + 1)%10 == int(S[2]) and (int(S[2]) + 1)%10 == int(S[3]):
    print("Weak")
    exit()

print("Strong")