import itertools
import string

def coins(x):
  pound=0
  #print x
  denoms=[1,2,5,10,20,50,100,200]
  for i in range(0,8):
    pound=pound+x[i]*denoms[i]
  if pound==200:
    return 1
  else:
    return 0
  

def getcoeff(xcoeff):
  def __getitem__(gen):
    return xcoeff[gen]
  for i in range(0,len(xcoeff)):
    yield xcoeff[i]
  
coeff=range(100)
coeff= itertools.product(coeff,repeat=8)
#print len(list(coeff))
#print len(coeff)
#print coeff[0]
count=0
for i in coeff:
  #print i
  count=count+coins(i)
  #print getcoeff(coeff[i])[i]
print count
