# Reading a file in Python
# file = open('data.txt', 'r')

# print(file.read())

# file.close()

# Writing to a file in Python
# file = open('data.txt', 'w')
# file.write("Hello, SHivaraj!")
# file.write("\nWelcome to Python programming.")
# file.close()

# Appending to a file in Python
# file = open('data.txt', 'a')
# file.write("\nNew Line added.")
# file.write("\nAnother line added.")
# file.close()

# with statement for file handling
# with open('data.txt', 'r') as file:
#     content = file.read()
#     print(content)
# with open('data.txt', 'w') as file:
#     file.write("This is a new file created using with statement.")
# with open('data.txt', 'a') as file:
#     file.write("\nAppending another line using with statement.")

# Task 1
total = 0
with open('sales.txt', 'r') as file:
    for line in file:
        total += int(line)
print(total)