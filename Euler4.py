z=[]
for i in range(100,1000):
    for j in range (100,1000):
        z.append(i*j)

z=sorted(set(z))

z= [str(i) for i in z]
z= [int(i) for i in z if i== i[::-1]]
z=max(z)
print(z)