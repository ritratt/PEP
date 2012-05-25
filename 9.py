import random

def PyK():
  triplets=[]
  while sum(triplets)!=1000:
    triplets=[]
    for i in range(0,3):
      triplets.append(random.randint(1,1000))
  #print 'Triplet found!'
  triplets.sort()
  #print triplets
  if(triplets[0]+triplets[1]<triplets[2]):
    return 0
  a=triplets[0]
  b=triplets[1]
  c=triplets[2]

  if(c**2==a**2+b**2):
    print triplets
    return 1
  else:
   # print 'bleh'
    return 0
  
x=0  
while(x!=1):
  x=PyK()
   