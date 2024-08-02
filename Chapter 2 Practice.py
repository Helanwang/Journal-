for i in range(1, 21):
    print(i)

print(round(6.6))  # 7

print(round(3.5, 2))
print(round(3.456, 2))  # Rounds to 2 decimal places: 3.46
print(round(3.456, 1))  # Rounds to 1 decimal place: 3.5
print(round(3.456, 0))  # Rounds to the nearest integer: 3.0
print(round(3.456))     # Rounds to the nearest integer: 3
print(round(3.5))       # Rounds to the nearest integer: 4

print(round(3.123423423, 2))  # output: 3.12
#  2 means, rounds to 2 digits here.

print(round(2))

print(round(0.1, 1))  # output: 0.1

""""""
base = 7
height = 3.5



# TODO: Calculate area
area = (base*height)/2
print("Step 1:", area)

# TODO: Round area to one decimal place
area_2 = round(area, 1)
print("Step 2:", area_2)

# TODO: Round area to nearest integer
area_3 = round(area, 0 )
print("Step 3:", area_3)


"""
floor division:  //
Computes the quotients. 

"""
number = 239
floor_division = number // 70
remainder = number % 70
print(f"when {number} / by 70. The quotients of {number} is"
      f" {floor_division}, the remainder is {remainder}")
# because 70 can only goes into 239, 3 times.
# come back and do exercise 2.5

"""
import math, for the sqrt() : square root function. 
"""
