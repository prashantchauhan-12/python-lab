a=int(input("enter side:"))
b=int(input("enter side:"))
c=int(input("enter side:"))

if(a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b):
    print("it is right angled triangle")
else:
    print("it is not a right angled triangle")