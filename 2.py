x=2
a=1
b=1
y=0

while(x<4*10**6):
  b=x
  x=x+a
  a=b
  if (x%2==0):
    y=y+x
print y  
#  1 1 2 3 5 8 