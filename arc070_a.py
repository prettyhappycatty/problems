# 0 0 
# 1 1 
# 2 2 
# 3 2 1+2
# 4 3 1+3  
# 5 3 2+3
# 6 3 1+2+3
# 7 4 1+2+4 or 3+4

X = int(input())

#等左数列の数の和がXを超えるnを見つける
n = 0
wa = 0
while wa < X:
    wa = n*(n+1)/2
    n += 1

print(n-1)