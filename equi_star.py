#.if the user input 3
#.   *
#.  * *
#. * * *

user=int(input("Enter the number of rows"))
row=user
#for number of rows
for i in range(1,user+1):
    #for space
    j=row
    while j-1>0:
        print(" ", end="")
        j-=1
    #for star
    k=1
    while k<=i:
        print("* ",end="")
        k+=1
    row-=1
    print()

    