import random

number = random.randint(0, 101)
user_number = input("Try to guess the number rom 0 to 100: ")
while int(user_number) != number:
    if int(user_number) > number:
        user_number = input("Your number is too big. Try once again: ")
    else:
        user_number = input("Your number is too small. Try once again: ")
else:
    print("Congratulations, you won!")
