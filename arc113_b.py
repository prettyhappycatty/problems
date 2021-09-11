a, b, c = map(int, input().split())
#A = int(str(a)[-1])<-こっちでもいいらしい（文字列配列の一番右）
A = a % 10
 
C = c % 4
if C == 0:
    C = 4
    
B = pow(b, C)
Bb = B % 4
if Bb == 0:
    Bb = 4
x = pow(A, Bb)
print(x%10)