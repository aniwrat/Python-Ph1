#nums=[1, 2, 2, 3, 4, 4, 4, 5]
#then output should be [2,4]

nums=[1, 2, 2, 3, 4, 4, 4, 5]
new_nums=[i for i in nums if nums.count(i)>1]
print (new_nums)