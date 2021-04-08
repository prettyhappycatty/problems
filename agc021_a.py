N = input()

if N.count('9') == len(N) or (N.count('9') == len(N) -1 and N[0] != '9'):
    #たすだけ ex) 5999
    keta = int(N[0]) + (len(N)-1)*9
else:
    #2つ以上9じゃないのがある ex) 5431->4999, 9449->8999, 4499->3999
    keta = int(N[0])-1 + (len(N)-1)*9

print(keta)