#NEAREST POINT IN 3D COORDINATE SYSTEM

points=[]#empty list to store points
npoints=[]#to store near points
print("enter 10 points in 3D coordinate")

#ENTRY FROM USER

for i in range(3):
    x=int(input("enter x coordinate\t"))
    y=int(input("enter y coordinate\t"))
    z=int(input("enter z coordinate\t"))
    points.append([x,y,z])

#PRINTING ENTERED LIST

print(points)    

#CALCULATING NEAR POINTS

nearest=[]
for i in points:
    min=float('inf')
    for j in points:
        if i==j:
            continue
        else:
            a=(i[0]-j[0])**2
            b=(i[1]-j[1])**2
            c=(i[2]-j[2])**2
            dis=(a+b+c)**(1/2)
            if dis<min:
                nearest=list(j)
    npoints.append([i,nearest])            

#PRINTING FINAL LIST

print(npoints)

print("pairing according to nearest points")
for i in range(0,3):
    print(points[i],"is most near to",npoints[i][1])
    
    