a=int(input("press 1 to convert celcius to farhenheit\npress 2 to covert farhrenheit to celcius\n"))

if(a==1):
    c=int(input("enter temp in celcius:"))
    f=c*9/5+32
    print("temperature in farhenheit is: ",f)
elif(a==2):
    f=int(input("enter temp in farhenheit:"))
    c=(f-32)*5/9
    print("temperature in farhenheit is: ",c)
