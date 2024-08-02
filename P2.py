x = 4.5
print(int(x))

print(str(x))

""""""
exam_1 = 93.0
exam_2 = 84.0
exam_3 = 85.5

average = (exam_1 + exam_2 + exam_3) / 3
print(float(average))
print(int(average))

""""""
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

result = x * y
print(float(result))

""""""
x = 3
y = "2"
result = x + int(y)

print(result)

print("50"*3)  # output: 505050

print(2*"this")  # output: thisthis
# print(2.0*"this") Output: error
# String repetition only works with strings and integers.

""""""
num = 2
user = input()
print(str(num) + "." + str(user))

""""""

# input:
# Quoth the Raven:
# "Nevermore"
# 3

# output:
# Quoth the Raven: "Nevermore"
# 3

str1 = str(input())
str2 = str(input())
int1 = str(input())

print(str1 + " " + str2 + "\n" + int1)  # "\n" means start a new line.

"""
OverflowError: 
result is too large
the value is larger than the upper limit of the floating-point range.

Runoff Error: 

"""