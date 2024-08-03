"""
Write a program that reads in a string, "lunch" or "dinner", representing the menu choice,
 and an integer, 1, 2, or 3, representing the user's meal choice.
 The program then prints the user's meal choice.
"""

user_choice = input("lunch or dinner?")

if user_choice == "lunch":
    print("Lunch menu")
    print("1, 2, or 3?")
    user_choice2 = int(input("what would you like on the lunch menu?"))
    if user_choice2 == 1:
        print("Caesar salad")
    elif user_choice2 == 2:
        print("Spicy chicken wrap")
    elif user_choice2 == 3:
        print("Butternut squash soup")
    else:
        print("invalid choice")
else:
    print("Dinner menu")
    print("1, 2, or 3?")
    user_choice3 = int(input("what would you like on the dinner menu?"))
    if user_choice3 == 1:
        print("Baked salmon")
    elif user_choice3 == 2:
        print("Turkey burger")
    elif user_choice3 == 3:
        print("Mushroom risotto")
    else:
        print("invalid choice")

"""Another approach"""
menu_choice = input("lunch or dinner")
meal_choice = int(input("what would you like on the menu?"))
order = ""
if menu_choice == "lunch":
    if meal_choice == 1:
        order = "Caesar salad"
    elif meal_choice == 2:
        order = "Spicy chicken wrap"
    else:
        order = "Butternut squash soup"

if menu_choice == "dinner":
    if meal_choice == 1:
        order = "Baked salmon"
    elif meal_choice == 2:
        order = "Turkey burger"
    else:
        order = "Mushroom risotto"

print(f"You have order {order}")


