def average ( x,y):
    return (x+y)
#test of the function with two numbers
numb1 = 33
numb2 = 45

result = average(numb1, numb2)
print("the average of{} and {} is ". format(numb1,numb2, result))

#part 11
# Input three numbers from the user
num1 = float (20)
num2 = float (44)
num3 = float (22)

# Find the minimum number
min_number = min(num1,num2,num3)

# Display the minimum number
print(f"The minimum number is: {min_number}")



# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the minimum number
min_number = min(num1, num2, num3)

# Display the minimum number
print(f"The minimum number is: {min_number}")