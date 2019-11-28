import time as t
import itertools as iter
bt= t.time()


#------------
def paully_the_pally_finder(int1,int2,num_of_products=2):
    l=[]
    a=list(iter.permutations(range(int1,int2,-1),num_of_products))
    for i in a:
        s= str(i[0]*i[1])
        if s == s[::-1]:
            l.append(s)
        if len(l)>30:
            print(sorted(l),i[0],i[1])
            break
#-------------
    
paully_the_pally_finder(1000,317,2)
ft= t.time()
print(round((ft-bt),5))
