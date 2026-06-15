# def greet(name, age, city, salary):
#     print("Hello", name)
#     print("Age:", age)
#     print("City:", city)
#     print("Salary:", salary)

# greet("Shivaraj", 25, "Bangalore", 50000)


#operators
# def opp(a, b):
#     print("Addition:", a + b)
#     print("Subtraction:", a - b)
#     print("Multiplication:", a * b)
#     if b != 0:
#         print("Division:", a / b)
#     else:
#         print("Division: Cannot divide by zero")

# opp(10, 5)

# Task
# Product_name = input("Enter product name: ")
# Price = float(input("Enter price: "))
# Quantity = int(input("Enter quantity: "))
# Total_cost = Price * Quantity
# print("Product Name:", Product_name)
# print("Price:", Price)
# print("Quantity:", Quantity)
# print("Total Cost:", Total_cost)
# Other Method using function
# Product_name = input("Enter product name: ")
# Price = float(input("Enter price: "))
# Quantity = int(input("Enter quantity: "))
# def calculate_total_cost(price, quantity):
#     return price * quantity

# Total_cost = calculate_total_cost(Price, Quantity)
# print("Product Name:", Product_name)
# print("Price:", Price)
# print("Quantity:", Quantity)
# print("Total Cost:", Total_cost)

# task1
# def square(num):
#     return num * num

# result = square(6)
# print("Square of 5 is:", result)

# task2
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = is_even(number)
print(f"The number {number} is {result}.")
