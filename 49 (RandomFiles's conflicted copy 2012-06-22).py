import itertools

def isPrime(n):
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
    return True




primeset=[2,3,5,7]
for i in range(10,1000):
    if isPrime(i):
        primeset.append(i)

subset = itertools.combinations(primeset,5)
print subset
