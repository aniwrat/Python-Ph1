#count duplicates in a list
#items =[1, 2, 2, 3, 4, 4, 4, 5]
#output- [2, 4]

items=[1, 2, 2, 3, 4, 4, 4, 5]
new_items=[]
ind=0
z=0
k=0
while ind< len(items):
    var=items[ind]
    #check equivalence of var with every other element of list
    for i in range(ind+1, len(items)):
        if(var == items[i]):
            if var not in new_items :
                new_items.append(var)
                break
    ind+=1
print(new_items)
