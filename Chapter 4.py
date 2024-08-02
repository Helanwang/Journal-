"""
Write a program that reads in an integer and prints whether the integer is even or not.
 Remember, a number is even if the number is divisible by 2. To test this use number % 2 == 0.
 Ex: If the input is 6, the output is "6 is even: True".
"""

number = int(input("Here"))
if number % 2 == 0:
    print("True")
else:
    print("False")

""""""
num = int(input())

is_even = (num % 2 == 0)
print(is_even)

print(0 == 1)
# false. When using comparison operator, it will return bool

""""""
# if statement
grade = input("what is your grade in letter")

if grade == "A":
    print("you are good for Berkeley")

else:
    print("you are not good enough")

# analyze which line of code is executed..
""""""
positive_num = int(input("Enter a positive number:"))
if positive_num < 0:
  print("Negative input set to 0")
positive_num = 0
print(positive_num)

# it didn't save the user's input because positive_num is set to 0. it didn't use += operator.

num = int(input())
den = int(input())

if den == 0:
    den = int(input())

result = num / den


print(result)

"""
and: both statement has to true to run the indented code. 
or: only one line has to true to run the indented code.
"""

