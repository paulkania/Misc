#Q1 not shown here.
#very intelligent backwards dstring via array[None]*len(string) then yah...maybe ill do it right now
#edit: that didnt take long
#this improves space complexity because instead of creating a new string each iteration of the for loop--> w/ s='' for el in string: s= el+ s (prepend so its backwards)
    #we instead create 1 array and add to it, giving much better space complexity.
string='rozehnal'
s_length = len(string)
s_index=len(string)-1
_output =[None]*len(string)
for element in string:
    _output[s_index] = element
    s_index -=1

output = ''.join(_output)
print(output)


masterlist =[9,4,12,3,6]
partiallist =[3,6,9,4]
masterlist =[0,2,200,-2,5,9,4,12,3,6]
partiallist =[3,6,9,4]
masterlist = [-2, 0, 2, 3, 5, 6, 7, 9, 12, 200]
partiallist =[7, 6,4, -2]


#this version works with partial lists that have been salted with garbage numbers.
#v1/2 - go n^2 time. go through each until thjere is a match, if there is no match,m add that number to a nomatch list.
missing=[]
for mnum in range(len(masterlist)):
    match=False
    for pnum in range(len(partiallist)):
            print((pnum,mnum))
            if partiallist[pnum]==masterlist[mnum]:
                print(partiallist[pnum],'is in the master list')
                match = True
                break
                # del partiallist[pnum]
                # del partiallist[mnum]

                break
    if not match:
        missing.append(masterlist[mnum])

print(sorted(missing))




masterlist =[0,2,200,-2,5,9,4,12,3,6]
partiallist =[3,6,9,4]
masterlist = [-2, 0, 2, 3, 5, 6, 7, 9, 12, 200]
partiallist =[7, 6, -2] #doesnt work if there are values in pl that are not in ml...but that wasnt part of q.


#v2/2 sort the lists and then match by 0th index. they align. this version feels a bit like cheating. plus its not effeicient since u have to sort both lists prior to comparison
masterlist=sorted(masterlist)
partiallist=sorted(partiallist)
missing_nums =[]
while partiallist:# and masterlist:
    print('m',masterlist)
    print('p',partiallist)
    print()
    if partiallist[0] == masterlist[0]:
        del partiallist[0]
        del masterlist[0]
        continue
    elif partiallist[0] != masterlist[0]:
        missing_nums.append(masterlist[0])
        del masterlist[0]
    # print(missing_nums)

#the rest of the masterlist belongs in the group, now that partial list runs out of values
for value in masterlist:
    missing_nums.append(value)
print('these are missing ->',missing_nums)
