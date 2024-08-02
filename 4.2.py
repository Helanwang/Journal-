speed = int(input("enter your speed"))


if 45 < speed < 70:
    print("Good driving")

else:
    print("follow the speed limit")


"""Operations Precedence"""

"""chained decision"""
wavelength = int(input("please enter wavelength"))

if wavelength in range(380, 450):
    print("Violet")
elif wavelength in range(450, 485):
    print("BLue")
elif wavelength in range(485, 500):
    print("Cyan")
elif wavelength in range(500, 565):
    print("Green")
elif wavelength in range(565, 590):
    print("Yellow")
elif wavelength in range(590, 625):
    print("orange")
elif wavelength in range(625, 750):
    print("red")
else:
    print("you are out of range")
