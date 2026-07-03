nums=[23, 99, 12, 150, 45]
max=nums[0]
s=len(nums)
i=1
while i!= s-1:
    if nums[i]>max:
        k=i
        max=nums[i]
    i=i+1


print(f"Maximum number in the list is {max} at index {k}")

