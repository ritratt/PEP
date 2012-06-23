
def pal(n):
    decimal=n
    binary=bin(n)
    if(str(decimal)==str(decimal)[::-1] and str(binary)[2:]==str(binary)[:1:-1]):
        return True
    else:
        return False

count=0

for i in range(0,1000001):
    if(pal(i)):
        count+=i

print count        
