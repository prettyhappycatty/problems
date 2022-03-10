S = input()


def isKaibun(s):
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False

    for i in range(len(s)//2):
        #print(s[i], s[-i-1])
        if s[i] != s[-i-1]:
            return False
    return True


#print(isKaibun("abs"))
#print(isKaibun("aba"))
#print(isKaibun("abccba"))



#後ろからaの数を数える。
N = len(S)

#最初から回文
if isKaibun(S):
    print("Yes")
    exit()

#最後がaでなければaを足すことで回文にはできない
if S[-1] != "a":
    print("No")
    exit()

i = 1
while S[-i] == "a":
    i += 1


j = 0
while S[j] == "a":
    j += 1

#print(i)
#print(j)

S = "a"*(i-j-1) + S

if isKaibun(S):
    print("Yes")
else:
    #print(S)
    print("No")