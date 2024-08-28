a=input("enter number to check for palindrome:")
if a==a[::-1]:
    print("yes it is palindrome\n")
else:
    print("no it is not palindrome\n")

# frequency dictionary
s=set(a)

for i in s:
    x=a.count(i)
    print(i," appear ",x," times")

