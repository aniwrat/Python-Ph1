#check armstrong number
#say 1221 take 1³ + 2³ + 2³ + 1³
print("Input a number : ")
o_num=int(input())
num=o_num
sum=0
#for the size of the number
t=str(o_num)
size=len(t)

while num!=0:       
    temp=num%10     
    print(temp) 
    sum=sum + temp**size 
    #mark this step division is always in float
    num=int(num/10)  
print(f"Calculated number is {sum}")
if(o_num == sum):
    print("Armstrong number")
else:
    print("not an Armstrong number")