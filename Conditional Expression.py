"""conditional expression executed in a single line code"""
# example here (before)

cards = int(input("here"))

if cards > 5:
    print(f"you have {cards} to play the game")
else:
    print("you do not have enough to play")

# after: this is conditional statement

cards = int(input("here"))
print(f"you have {cards} to play the game") if cards > 5 else print(f"you don't have enough to play")

# input: 10
# You have 10 cards to play the game.


