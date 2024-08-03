# script.py

def count_spaces(user_input):
    count = 0
    for i in user_input:
        if i == " ":
            count += 1
            print(f"Found a space, count is now {count}")
    print(f"Total count of spaces is {count}")


user = input("Count space here: ")
count_spaces(user)
