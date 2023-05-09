import random

number = random.randint(0, 201)
user_number = input("Try to guess the number rom 0 to 200:")
while int(user_number) != number:
    if int(user_number) > number:
        user_number = input("Your number is too big. Try once again:")
    else:
        user_number = input("Your number is too small. Try once again:")
else:
    print("Congratulations, you won!")
