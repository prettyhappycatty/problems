a,b = map(int, input().split())

#関数を定義
def gcd(a,b): 
#①のとき
    if b == 0:
        return a
#②のとき
    else:
        return gcd(b,a%b)
#結果を出力
print(gcd(a,b))