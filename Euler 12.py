###really really slow

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
            
trif(3483480)
# 
# for i in range(1,1000000):
#     trif(i)
# 2031120(240),2162160(320),3483480(256)



# while c<500:
#     for i in range(1,trif+1):
#         c=0
#         if (trif%i)==0:
#                  print(i)
#             c+=1
#             print(c)
#             if c>500:
#                 print(i,c)

    
#     
#     
# def triangle(a,b=1):
#     c=0
#     if a==1:
#         for i in range(1,(b+1)):
#             if (b)%i==0:
#                 print(i)
#                 c+=1
#                 if c > 500:
#                     return b, c, 'b,c triWER FOUND'
#         return b,c,'b(tri),c(# of divisors)'
# 
#     else:
#         print(b,'b', '\n', c,'c else-loop','\n','_-_-_-_-_')
#         return triangle(a-1,a+b)
# 
# # print(triangle(5000))
# # print(my_triangle(5000))
