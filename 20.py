print reduce(lambda a,b:int(a)+int(b), list(str(reduce(lambda x,y:x*y,range(100,1,-1)))))
