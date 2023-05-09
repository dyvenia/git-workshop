import random

number = random.randint(0, 101)
user_number = int(input("Try to guess the number rom 0 to 100: "))
while user_number != number:
    if user_number > number:
        user_number = int(input("Your number is too big. Try once again: "))
    else:
        user_number = int(input("Your number is too small. Try once again: "))
else:
    print("Congratulations, you won!")
