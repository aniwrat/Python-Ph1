#print number 1-50
#multiple of 3 "Fizz"
#multiple of 5 "Buzz"
#multiple of 3 and 5 "FizzBuzz"
i=1
for i in range (50):
    if i%3==0 and i%5==0:
        print("FizzBuzz \n")
        
    elif  i%5 ==0:
        print("Buzz \n")
        
    elif i%3==0 :
        print("Fizz \n")
        
    else :
        print(f"{i}\n")
