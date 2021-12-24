S = input()
T = input()

first = (ord(S[0])-ord(T[0]) + 26 ) % 26
for i in range(1, len(S)):
    #print(ord(S[i])-ord(T[i]))
    if (ord(S[i])-ord(T[i]) + 26) % 26 != first:
        print("No")
        exit()

print("Yes")