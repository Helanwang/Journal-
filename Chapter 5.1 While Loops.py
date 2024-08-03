# Initialization
x = 10


while x < 10:
    # Loops body
    print(x)
    x += 1
#   it will not go to the next line until the loop body is finished

print("end of loops")
# it will execute this line when loop is finished.
# if condition is false, it will print directly this line

count = 8
while count != 0:
    print(count * "*")
    count -= 1

print("end of loops")

# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
# end of loops

user = input("Enter begin")

while user != "begin":
    print(user)
    input("you enter" + user)

print("you have entered begin")

# for loops
user = str(input("Count Space here."))

count = 0
for i in user:
    if i == " ":
        count += 1
        print(count)

print("you total count of space is", count)

# do exercise 5.2 later. Another harder for loops question.

