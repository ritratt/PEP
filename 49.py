import itertools

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def getprimes(x):
  #print x
  concats=itertools.permutations(x,2)
  for i in concats:
    i=map(str,i)
    i=''.join(i[:])
    i=int(i)
    if not isPrime(i):
      return False
  return True


primeset=[3,7]
for i in range(10,1000):
    if isPrime(i):
        primeset.append(i)
print len(primeset)
subset = itertools.combinations(primeset,4)

count=0
for i in subset:
  count+=1
  #print count
  if(getprimes(i)):
    print 'zomg!'
    print i
