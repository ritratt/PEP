def threefacts(x):
  fact=[]
  for j in range(100,999):
    if(x%j==0 and len(str(x/j))==3):
      print j
      print x/j
      print x
      return True
      

for i in range(999*999,0,-1):
  if(str(i)==str(i)[::-1]):
    #print i
    if(threefacts(i)):
      break;


  