x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

rr = r**2

def dist2(xx1, yy1, xx2,yy2):
    return (xx2-xx1)**2 + (yy2-yy1)**2


def in_circle():
    overrap = False
    s_include_c = False
    c_include_s = False
    if dist2(x1, y1, x2,y2) <= rr and dist2(x1, y1, x2,y3) <= rr and dist2(x1, y1, x3,y3) <= rr and dist2(x1, y1, x3,y2) <= rr :
        #頂点が全て円の内部
        c_include_s = True
    elif dist2(x1, y1, x2,y2) <= rr or dist2(x1, y1, x2,y3) <= rr or dist2(x1, y1, x3,y3) <= rr or dist2(x1, y1, x3,y2) < rr :
        #頂点の1つ以上が円の内部
        overrap = True
    elif (abs(x1 - x2) < r and y2 < y1 < y3) or (abs(x1 - x3) < r and y2 < y1 < y3):
        #辺が円の内部  
        overrap = True
    elif (abs(y1-y2) < r and x2 < x1 < x3) or (abs(y1-y3) < r and x2 < x1 < x3):
        #辺が円の内部
        overrap = True

    if x2 <= x1 <= x3 and y2 <= y1 <= y3 and  x3-x1 >= r and x1 - x2 >= r and y3 - y1 >= r and y1 - y2 >= r:
        s_include_c = True

    return overrap, s_include_c,c_include_s

ov, inc_c, inc_s = in_circle()

if inc_s == True:
    print("YES")
    print("NO")
elif inc_c == True:
    print("NO")
    print("YES")
else:
    print("YES")
    print("YES")

#print(in_circle())
