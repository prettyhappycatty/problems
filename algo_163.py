s = "100010101"

def change2to10(s):#sはString
    sum2 = 0
    j = 0
    for i in range(len(s)-1, -1, -1):
        sum2 += int(s[i])*(2**j)
        j += 1
    return sum2

print(change2to10(s))