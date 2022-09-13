import random
number = random.randint(0, 101)
my_number= input("Try to guess the number rom 0 to 100:")
while int(my_number) != number:
    if int(my_number) > number:
        my_number = input("Your number is too big. Try once again:")
    else:
        my_number = input("Your number is too small. Try once again:")
else:
    print("Congratulations, you won!")
   
   
