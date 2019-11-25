#Leo

trinum = 1
for i in range(2, 1000000000000): #essentially a while loop.
    trinum = trinum + i  # 1+2+3+4+5+6
    div =2
    half = trinum // 2 #since max divisor is trinum//2 (works since trinum is only whole numbers)
    num = 100 #???
    for d in range(2, half):
        if d >= num:
            break
        if trinum % d == 0:
            num = trinum // d
            div = div + 2 #what trick is there that i would do +1
        if d * d == trinum: #why?
            div -= 1 #

    if div > 500:
        print("FOUND:")
        print(trinum)
        break

####via summming

import time
start_time = time.time()

import functools as fn

# def my_triangle(tri):

def tri_f(top):
    c=0

    summed_t=[]
    for i in range(top,0,-1):
        summed_t.append(i)
    # print(summed_t)
    s=sum(summed_t) #hey you can sum a list, hooray
    # print(s)# print(len(summed_t))
    for i in range(1,s+1):
        if (s%i)==0:
            c+=1
            print(i)
            # if c>200:
            #     print(summed_t,c,i, 'top,c,i')
            # if c>500:
            #     return('A', summed_t, c, i)



tri_f(10000)

fin_time=time.time()
d1=fin_time-start_time
print(d1)


##via fn.reduce

import time
start_time = time.time()
import functools as fn


# def my_triangle(tri):

def trif(trif):
    c=0

    summed_t=[]
    for i in range(trif,0,-1):
        summed_t.append(trif)
        trif-=1
    trif=fn.reduce(lambda a,d: a+d, summed_t)
    for i in range(1,trif+1):
#         print('x hit')
        if (trif%i)==0:
            c+=1
#             print(i)
            if c>200:
                print(trif,c,i, 'trif,c,i')
            if c>500:
                return('A', trif, c, i)
            
trif(10000)
# 
# for i in range(1,1000000):
#     trif(i)



fin_time=time.time()
d1=fin_time-start_time
print(d1)
