nums=[2223, 99, 12, 1150, 45]
max=nums[0]
s=len(nums)
i=1
k=0
while i!= s-1:
    if nums[i]>max:
        k=i
        max=nums[i]
    i=i+1


print(f"Maximum number in the list is {max} ")

#for second remove the first then search for max
kk=nums.pop(k)
#print(k)
#print(nums)
#now search for max

s_max=nums[0]
ss=len(nums)
ii=1
while ii!= ss-1:
    if nums[ii]>s_max:
        #k=i
        s_max=nums[ii]
    ii+=1


print(f"Second Maximum number in the list is {s_max} ")
