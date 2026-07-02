#factorial of a number
num= int(input("Enter the number of which you want factorial : \n"))
a=num
temp=1
while a>=1:
    temp=temp*a
    a=a-1
print(f"factorial of {num} is {temp}")
