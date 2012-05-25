sum3=333*(3+999)/2
sum5=199*(5+995)/2
sum15=66*(15+990)/2
answer=sum3+sum5-2*sum15
print answer
x=0

for i in range(0,1000):
  if(i%3==0 or i%5==0):
    x=x+i

for i in range(0,1000):
  if(i%15==0):
    x=x-i

print x