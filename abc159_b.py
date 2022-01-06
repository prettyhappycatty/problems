s=input()

def is_kaibun1(S):
  for i in range((len(S)-1)//2):
    if S[i]!=S[len(S)-i-1]:
      return False
  return True

def is_kaibun2(S):
  for i in range((len(S))//2):
    if S[i]!=S[len(S)-i-1]:
      return False
    return True
    
#print(s[:(len(s)-1)//2],s[(len(s)+1)//2:])

if is_kaibun1(s) == False:
  print("No")
else:
  if is_kaibun2(s[:(len(s)-1)//2]) == False:
    print("No")
  else:
    print("Yes")