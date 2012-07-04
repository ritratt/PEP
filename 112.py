

def bouncy(n):
  reverse_n=list(str(n)[::-1])
  
  n1=list(str(n))
  n1.sort()
  n2=list(str(n))
  n=list(str(n))
  #print n1
  if(n!=n1 and reverse_n!=n1 ):
    #print n,sort_n,reverse_n
    return True
  else:
    return False
    

    
count=0.00
bouncy_count=0.00
i=0
while(True):
  count+=1
  i+=1
  if(bouncy(int(i))):
    bouncy_count+=1
    print bouncy_count/count
    if(bouncy_count/count==0.99 and count>1000):
      print count
      print bouncy_count
      break
      