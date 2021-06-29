#関数を定義
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcd(a,b):
    return a*b//gcd(a,b)