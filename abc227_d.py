N,K=map(int,input().split())
alist=list(map(int,input().split()))

dic={}

def func(x):

  if x in dic:
    return dic[x]
  asum=0
  for a in alist:
    asum+=min(a,x)
  return asum>=K*x

l=1
r=sum(alist)//K
while True:
  mid=(l+r)//2
  if func(mid) and not func(mid+1):
    print(mid)
    break
  elif func(mid):
    l=mid+1
  else:
    r=mid-1