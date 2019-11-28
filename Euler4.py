import time as t
import itertools as iter
from operator import itemgetter
bt= t.time()


#------------
def paully_the_pally_finder(int1,int2,num_of_products=2):
    l=[]
    elements=[]
    a=list(iter.permutations(range(int1,int2,-1),num_of_products)) #returns a list of tuples
    for i in a:
        s= str(i[0]*i[1])#i[0] refers to the first element of tuple i for i in range given.
        if s == s[::-1]: #comparing string with backwards string.
            l.append(int(s)) #int just for beautification of printed output
            elements.append(i)
        if len(l)>30:
            output = list(zip(elements,l))
            output = sorted(output,key=itemgetter(int(input('sort by 0-tuple or 1-product'))))
            for i in output:
                print(i)
            break
#-------------
    
paully_the_pally_finder(1000,317,2)
ft= t.time()
print(round((ft-bt),5))

