#List
# fruits = ["apple", "banana", "orange"]
# fruits.append("grape")
# print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

#Tuple
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(days)  

#List Example 1
# employees = ["Alice", "Bob", "Charlie", "David", "Eve"]
# employees.remove("Charlie")  # Remove "Charlie" from the list
# # employees.append("Frank")
# print(employees)  # Output: ['Alice', 'Bob', 'Charlie', 'David
# print(len(employees))  # Output: 5
# print(employees[1])

# for loop in list
# for employee in employees:
#     print(employee)

# Task 1
# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# for city in cities:
#     print(city)

# task 2
# marks = [85, 92, 78, 90, 88]
# total_marks = 0
# for mark in marks:
#     total_marks += mark
# print("Total marks:", total_marks)


# Task 3
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("You entered:", numbers)
print(max(numbers))  # Output: The maximum number entered