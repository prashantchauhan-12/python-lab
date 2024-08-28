import math
def ballCollide(b1,b2):
    a=b1[0]-b2[0]
    b=b1[1]-b2[1]

    dist=math.sqrt(a*a+b*b)
    if(dist<=b1[2]+b2[2]):
        print("they collide!!!\n")
    else:
        print("they don't collide!!!\n")

b1=(3,4,5)
b2=(2,3,5)

ballCollide(b1,b2)