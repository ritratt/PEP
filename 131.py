
def isCube(n):
    n = ((float(n)**(1.0/3.0)))
    print n%1.0
    if(n%1.0==0.0):
        return True
    else:
        return False

def getCube(n):
    i=0
    while(cube<n):
        cube=i**3
        i+=1
        yield cube
def isPrime(p):
    for i in range(2,int(p**0.5+1)):
        if p%i==0:
            return False
    return True

def sFactor(prime,cubes):
    i=1
    expression=0
    for i in cubes:
        #print i
        #expression=i**3 + (i**2)*prime
        partial_exp=i+prime
        #print expression
        if (cubes.count(partial_exp))>0:
            if isPrime(prime):
                print prime
                return i
        #elif i>100:
            #break
        #i+=1
cubes=[]
for i in range(500,600):
    cubes.append(i**3)
#primes=[j for j in range(2,1000000) if isPrime(j)]
#print primes

special_pairs={}
for m in range(742519,1000001,2):
    #print m
    if(sFactor(m,cubes)):
        special_pairs[m]=sFactor(m,cubes)
        #print special_pairs

print special_pairs

