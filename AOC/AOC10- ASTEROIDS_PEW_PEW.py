import os
import math

def part1(amatrixwidth,filename):
    os.chdir(r"C:\Users\proze\Desktop\coderun")
    with open(filename+'.txt','r') as f:
        data = f.read()
    # print(1,data)
    mapstring=data.replace('\n','')
    # print(2,mapstring)
    visited_angle = []
    maxasteroidcount = 0
    iterativeasteroidcount = 0
    maxpos=(0,0)
    # matrixwidth=20
    angle = 0
    for index in range(len(mapstring)):
        if mapstring[index] == '#':
            currentstation = index
            xi = currentstation % amatrixwidth
            yi = currentstation // amatrixwidth
            for index2 in range(len(mapstring)):  ##(then check the whole array again)
                if mapstring[index2] == '#':
                    xf = index2 % amatrixwidth
                    yf = index2 // amatrixwidth
                    # print(index2)
                    if xf-xi !=0 or yf- yi!=0:
                        angle = math.atan2((yf - yi) , (xf - xi))
                        angle = round(angle,10)
                        # print(angle) ####WATCH for radians
                    if angle in visited_angle:
                        continue  ####this got t check the whole arr, butnxt_indx
                    visited_angle.append(angle)
                    iterativeasteroidcount += 1

            # after done checking all map do w want this in line with ‘top if’ or second ‘for’?
            if iterativeasteroidcount > maxasteroidcount:
                maxasteroidcount = iterativeasteroidcount
                maxpos=(xi,yi)
            iterativeasteroidcount = 0
            visited_angle=[]
    return maxpos ,maxasteroidcount

# print(part1(5,'a-5'))

#GOT EM
# print(maxasteroidcount+1)
#test X - Myscore   / RealScore
#test 1 PASS FAIL############################
#test b_10 33 ###5,8 Pass,Pass
#t2 - c_10 35,(1,2) Pass,Pass
# t3 - d_10  41,(6,3) - Pass,Pass
#t4 -  e_20 210,(11,13) -pass,pass
# final     221(11,11) - pass, unknown
#
def part2(afilename,amatrixwidth,xhome,yhome):
    os.chdir(r"C:\Users\proze\Desktop\coderun")
    with open(afilename + '.txt', 'r') as f:
        data = f.read()
    mapstring = data.replace('\n', '')

    allasteroids=[]
    asteroid_dict={}
    current_asteroid_angle =-0.1 #anything under 0
    planet_smasher_counter = 0
    anslist= []
    for index in range(len(mapstring)):
        if mapstring[index] == '#':
            currentstation = index
            xast = currentstation % amatrixwidth
            yast = currentstation // amatrixwidth
            mahanttan_distance = abs(xast-xhome)+abs(yast-yhome)
            if mahanttan_distance !=0:
                angle = round(math.atan2((yhome - yast), (xhome - xast)),20)
                print('a1',angle)
                if angle >=0: #creating a cohesive circle range instead of a negative and positive
                    angle=round(angle*(360/(2*math.pi)),8)
                    print('a>0',angle)
                else:
                    angle = round((2*math.pi +angle)*(360/(2*math.pi)),8)
                    print('a<0',angle)
                if angle <90: #starting the circle at the top instead of at the left.
                    angle = angle+270
                else:
                    angle = angle-90
                allasteroids.append((angle,mahanttan_distance,(xast,yast)))
    allasteroids=sorted(allasteroids,key=lambda x : (x[0],x[1]) ) #keyline - I can sort by x[0] initially, and then x[1] if there are x[0]'s that are equal.
    for ast in allasteroids: #turned the list into a visited-type dict.
        asteroid_dict[ast] = False
    while len(allasteroids) > planet_smasher_counter: #until all planets have been smashed.
        for tuple,visited in asteroid_dict.items():
            circlereset = False #checker to see if the circle should be reset to 0
            if tuple[0] > current_asteroid_angle and asteroid_dict[tuple] == False:
                # print('sdsdsdsds',tuple[0])
                circlereset = True #avoid circle reset since an anglelarger than current asteroid angle exists
                asteroid_dict[tuple] = True #mark as visited
                anslist.append(tuple)
                current_asteroid_angle = tuple[0]
                planet_smasher_counter += 1
        if circlereset == False:
            current_asteroid_angle = -0.1
    
    return anslist

# print(part1(21,'fin21')) #gives 11,11, feed into part 2
# print()
x=part2('fin21',21,11,11)
count=1
for el in x:
    print(el,'---',count)
    count+=1
