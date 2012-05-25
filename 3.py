def prime(x):
  y=0
  for j in range(2,x/2):
    if(x%j==0):
      return False
    else:
      y=1
  if(y==1):
    return True
    
a=600851475143
a=int(a**0.5)+1
for i in range(a,0,-1):
  if(a%i!=0 and prime(i)):
    print i
    break
  
