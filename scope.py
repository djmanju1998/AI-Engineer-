# Local Variable Scope
# def order():
#     # Local variable
#     item = "Pizza"
#     print("Inside function:", item)

# # Call the function
# order()

# Enclosing Variable Scope
# def cart():
#     item = "Burger"
#     def order():
#         # Enclosing variable
#         print("Inside order function:", item)
#     order()
# # Call the cart function
# cart()

# Global Variable Scope
# item = "Pasta"  # Global variable

# def order():
#     print("Inside function:", item)

# def order1():
#     print("Inside order1 function:", item)

# # Call the functions
# order()
# order1()

# Built-in Variable Scope
# print(__file__)  