import itertools

def Sets():
    for i in range(1,101):
        yield i**2



def yield_set():
    test_set=[1,3,6,8,10,11]
    testC=itertools.combinations(test_set,3)
       
    sumset=map(sum,set(testC))
    sumset.sort()
    print sumset
    print sum(set(sumset))


square_set=map(lambda x:x**2,range(1,101))
yield_set()
