def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def lcm(x,y):
    temp=(x*y)/hcf(x,y)
    return temp

num1 = int(input("enter first number: ")) 
num2 = int(input("enter second number: "))

print("The H.C.F. is", hcf(num1, num2))
print("The L.C.M. is", lcm(num1,num2))

