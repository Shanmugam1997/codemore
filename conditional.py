number = int(input("Enter a number: "))

if number %2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# find positive or negative
number = int(input("enter a number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

#find largest number among three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))        
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)



