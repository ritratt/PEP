
def prime(x):
  y=0
  if(x==2 or x==3):
    return True
  for j in range(2,x/2+1):
    if(x%j==0):
      return False
    else:
      y=1
  if(y==1):
    return True
def primefacts(y):    
  fact=[]
  
  for i in range(2,y/2):  
    x=y
    while(x!=1):
      if(x%i==0 and prime(i)):
	fact.append(i)
	x=x/i
      else:
	x=1
  return fact
  
fact20=primefacts(20)
print fact20
print fact20.count(fact20[0])
x=filter(lambda a:a!=str(fact20[0]),fact20)
print x