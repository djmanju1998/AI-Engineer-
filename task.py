#Task 1
# name = "Shivaraj"
# print("Hello", name)

#Task 2
# name = input("Enter your name: ")
# print("Hello", name)
# age = input("Enter your age: ")
# age = int(age)
# print("You are", age, "years old.")

#Task 3
# num = 9
# if num % 2 == 0:
#     print(num, "is even.")
# else:
#     print(num, "is odd.")

#Task 4
# for i in range(1,11):
#     print(i)

#Task 5
# name = input("Enter your name: ")
# print("Hello", name)

#Task 6
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("The greater number is", num1)
# else:
#     print("The greater number is", num2)

#Task 7
# num = 6
# for i in range(1, 21):
#     print(num, "x", i, "=", num * i)

#Task 8
# def num(a,b):
#     return a * b

# result = num(2,7)
# print("The product is", result)

#Task 9
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
    print("The result is", result)
elif operator == "-":
    result = num1 - num2
    print("The result is", result)
elif operator == "*":
    result = num1 * num2
    print("The result is", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")