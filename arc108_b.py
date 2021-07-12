N = int(input())
s = input()
t = ""

i = 0
while i < N:
    tmp = s[0]
    t += tmp
    l = len(t)
    #print("fox?", t[l-3:l])
    if l>2 and t[l-3:l] == "fox":
        t = t[0:l-3]
    s = s[1:len(s)]
    i += 1
    #print(t)
    #print(s)

#print("s", s)
print(len(t))