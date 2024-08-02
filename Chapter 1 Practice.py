print("555", "0123", sep="-")

name = input()
print(f"hello, {name}")

"""1"""
print("I shall be telling this with a sigh")
print("Somewhere ages and ages hence")
print("two roads diverged in a wood, and I--")
print("I took the one less traveled by,")
print("And that has made all the difference.")

"""2"""

name = input("what is your name?")
fun = input("what do you like to do?")

answer = f"{name} likes to {fun}"
print(answer)

""""""

team_one = "Liverpool"
team_two = "Chelsea"
score_one = 4
score_two = 3
print(f"{team_one} versus {team_two}")
print("Final score:", score_one, "to", score_two)

print("you say 'please' to be polite.")
print(len("he she"))  # output: 6, including the space

print("1" + "0")  # output: 10

""""""
first = input("what is your first name?")
last = input("what is your last name?")

x = len(first)
y = len(last)

print(f"you first name is {x} letters long")
print(f"you last name is {y} letters long")

print("you first name is" + str(x) + "letters long")
print("you last name is" + str(y) + "letters long")

""""""
name = "Freda"
feel = "happy"
print(f"Hi {name}!")
print(f"I'm glad you feel {feel}")

""""""

print(list(range(1, 13)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

""""""
a = 3.5 - 2.5
print(a)

b = 20/10
print(b)

c = 2*1.5
print(c)

d = 4 * 3 ** 2 + 1
print(d)

""""""
int_a = 10
float_a = 10.0
string_a = "10"
print(int_a)
print(float_a)
print(string_a)

""""""
meters = 10
meter2feet = 3.28
feet = meters * meter2feet
print(feet)

""""""

for i in range(1, 7):
    print(i)

""""""

for i in range(1, 10):
    print(i)
"""

Docstrings notes: 

usually have three parts

summary line
one blank line
descriptions
"""