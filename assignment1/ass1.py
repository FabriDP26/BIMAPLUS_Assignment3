
n = int(input("Enter number of Points "))
#we want to store our x and y values, we start from x


x = [] 
y = []

for i in range(n):
   x.append(float(input("input x coordinates of point " + str(i+1) + ": ")))
   y.append(float(input("input y coordinates of point " + str(i+1) + ": ")))

print("Point\tx\ty")
print("-"*20)

for i in range(n):
    print(i+1,"\t",f"{x[i]:.1f}","\t", f"{y[i]:.1f}")


print("geometric characteristics:")
area = 0
for i in range(n):
    xi1 = x[i]
    xi = x[i-1]
    yi1 = y[i]
    yi = y[i-1]
    area = area + (xi1 + xi)*(yi1 - yi)
area = area/2
print("Ax: "f"{area:.2f}") 

smx = 0
smy = 0
for i in range(n):
    xi1 = x[i]
    xi = x[i-1]
    yi1 = y[i]
    yi = y[i-1]
    smx = smx + (xi1 - xi)*(yi1**2+yi*yi1+yi**2)
    smy = smy + (yi1 - yi)*(xi1**2+xi*xi1+xi**2)
smx = smx/-6
smy = smy/6
print("Sx: "f"{smx:.2f}") 
print("Sy: "f"{smy:.2f}") 


inex = 0
iney = 0
inexy = 0
for i in range(n):
    xi1 = x[i]
    xi = x[i-1]
    yi1 = y[i]
    yi = y[i-1]
    inex = inex + (xi1 - xi)*(yi1**3+yi1**2*yi+yi1*yi**2+yi**3)
    iney = iney + (yi1 - yi)*(xi1**3+xi1**2*xi+xi1*xi**2+xi**3)
    inexy = inexy + (yi1-yi)*(yi1*(3*xi1**2+2*xi1*xi+xi**2)+yi*(3*xi**2+2*xi1*xi+xi1**2))
inex = inex/-12
iney = iney/12
inexy = inexy/-24
print("Ix: "f"{inex:.2f}") 
print("Iy: "f"{iney:.2f}") 
print("Ixy: "f"{inexy:.2f}") 

xt = smy/area
yt = smx/area
print("xt: "f"{xt:.2f}") 
print("yt: "f"{yt:.2f}") 

ixt = inex-yt**2*area
iyt = iney-xt**2*area
ixyt=inexy+xt*yt*area
print("Ixt: "f"{ixt:.2f}") 
print("Iyt: "f"{iyt:.2f}") 
print("Ixyt: "f"{ixyt:.2f}") 
