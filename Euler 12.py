import sys
sys.setrecursionlimit(10000)

def triangle(a,b=1):
    c=0
    if a==1:
        for i in range(1,(b+1)):
            if (b)%i==0:
                print(i)
                c+=1
                if c > 500:
                    return b, c, 'b,c ANSWER FOUND'
        return b,c,'b(ans),c(# of divisors)'

    else:
        print(b,'b', '\n', c,'c else-loop','\n','_-_-_-_-_')
        return triangle(a-1,a+b)

print(triangle(5000))

#1i have the answer, but since it involved recursion
# 2 i have 2 problems
# 3 1 doing recursion w high #s takes a huge amount of memory
# 4 2 since it's recursion I can't run a loop until a trigger is hit
# 5 i have to instead guess, which is insane.

# 6 next to do -> create a simple factorial that doesnt require recursion
# 7 then implement that system into the above logic.
# first a mini-tour
