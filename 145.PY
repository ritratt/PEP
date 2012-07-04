
def isReversible(n):
    if(n%10==0):
        return 0
    final=n+int(str(n)[::-1])
    #if str(final)!=str(final)[::-1]:
        #return 0
    digits=getDigits(final)
    for i in digits:
        if not isOdd(i):
            return 0
    #print n
    return 1

def getDigits(m):
    for d in str(m):
        yield int(d)

def isOdd(o):
    if o%2==0:
        return False
    else:
        return True
    
count=0
for i in xrange(11,10**9):
    count+=isReversible(i)

print count
