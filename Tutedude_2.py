
# Task 1: Check if a Number is Even or Odd

num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    
    
# Task 2: Sum of Integers from 1 to 50 Using a Loop

sum = 0 
for i in range(1,51):
    print(i)
    sum = sum + i
    
print(f"The sum of all the integers is : {sum} ")
