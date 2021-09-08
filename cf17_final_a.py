S = input()

ary = ["KIH", "B", "R"]

tmp = S
i = 0
#KIHの前が、"A"か""であること"
if "KIH" not in tmp:
    print("NO")
    exit()

S1 = S.split("KIH",1)

#Bの前が、"A"か""であること"
if "B" not in S1[1] or (S1[0] != "A" and S1[0] != ""):
    print("NO")
    exit()

S2 = S1[1].split("B",1)

#Rの前が、"A"か""であること"
if "R" not in S2[1] or (S2[0] != "A" and S2[0] != ""):
    print("NO")
    exit()

S3 = S2[1].split("R",1)
#Rのあとが、"A"か""であること"
if S3[0] != "A" and S3[0] != "":
    print("NO")
    exit()
    
#Rのあとが、"A"か""であること"
if S3[1] != "A" and S3[1] != "":
    print("NO")
    exit()

print("YES")