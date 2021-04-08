A,B,C,X,Y = list(map(int, input().split()))

# A Aピザ円
# B Bピザ円
# C ABピザ円

# A+B  C*2との関係次第
# 

if A > C*2 or B > C*2:
    #A
    if Y>X:
        yen0 = C*2*X + (Y-X)*B
    else:
        yen0 = C*2*X 

    #B
    if Y>X:
        yen1 = C*2*Y 
    else:
        yen1 = C*2*Y + (X-Y)*A
    
    if yen1 > yen0:
        yen = yen0
    else:
        yen = yen1
    
elif A+B > C*2:
#    print('A+B > C*2')
    if X > Y: #Aピザの方が多い
#        print('Aピザ多い')
        yen = Y*C*2 + A*(X-Y)
    else:
        yen = X*C*2 + B*(Y-X)

else:
    yen = A*X + B*Y

print(yen)
