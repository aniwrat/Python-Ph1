#to find sum and average of a list 
#marks=[85, 90, 72, 60, 95] using loop
marks=[85, 90, 72, 60, 95]
size = len(marks)
sum=0
for i in marks:
    sum=sum+ i
print(f"The total is {sum}")
avg=int(sum/size)
print(f"The Average is {avg}")    
