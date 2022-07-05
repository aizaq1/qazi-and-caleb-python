# Data types are ways for us to store information

# Integers - whole numbers (negative or positive)
# 2
# 3
# 4
# ...
# -2
# -3
# -4

# Strings - store phrases or words that we want to have somewhere ; in quotations
# greeting = "Hello world"  # Variable
# print(greeting)

# print("\"Hello world\"")
# print('"Hello world"')

# Floats - decimal numbers
# 3.5
# 4.0
# 3.3
# 2.0
# 1.1
# rating = 4.9
# print(3.5)
# print(2.0)
# print(rating)

# Booleans - True / False
# True - capitilize
# False - capitilize

# Avoid the following
# true = "Hello"
# print(true)
# false = "Hi"
# print(false)
# Avoid the above

# 1 + 2  # addition
# 3 - 1  # subtraction
# 3 * 2  # multiplication
# 6 / 3  # division

# print(6/3*2+2-1*5)
# 6/3*2+2-1*5
# 2*2+2-1*5
# 4+2-1*5
# 4+2-5
# 6-5
# 1
# print(1+2)
# print(3-1)
# print(3*2)

# Input() allows users to enter infor
# mation
# input("Enter your age: ")

## REVIEW ##
# True - Boolean
# False - Boolean
# "Hi my name is John." - String
# 4.9 - Float
# 17 - Integer
# -20 - Integer
# print("9"*3)  # 999
# print("3"*3)  # 333
# print("5" * 5)  # 55555

# Type casting
# age = int(input("Enter your age: "))  # Input() is always going to make it a String
# print(age + 5)

# rating = float(input("Enter your rating: "))
# print(rating)

# answer = input("Do you like ice cream? ")
# print(answer)

# age = input("What is your age? ")
# # print("You are 9 years old")  # We want this
# print("You are " + age + " years old.")  # String concatenation

# answer = input("Do you like ice cream? ")
# Case 1: answer = "Yes"
# "Your answer was: Yes"
# Case 2: answer = "No"
# "Your answer was: No"
# print("Your answer was: " + answer)

# rating = float(input("Enter your rating: "))
# "You rated the restaurant _____ stars."
# # print("You rated the restaurant " + rating + " stars.")
# print(f"You rated the restaurant {rating} stars.")  # Formatted string

# answer = input("Do you like ice cream? ")
# print("Your answer was: " + answer)
# print(f"Your answer is : {answer}")
