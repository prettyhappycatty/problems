S = input()

#print(S[1:4])
st = 0
en = 3

m = int(S)
for i in range(len(S)-2):
    num = int(S[st+i:en+i])
    #print(num, 753-num)
    if m > abs(753-num):
        m = abs(753-num)

print(m)