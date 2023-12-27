import random

random_number = random.randint(0, 20)
guess_number = input("Enter your guess number: ")
guess_number = int(guess_number)
while guess_number != random_number:
    if random_number > guess_number:
        print("Your guess is less than random number")
    else:
        print("Your guess is greater than random number")
    guess_number = input("Enter your guess number: ")
    guess_number = int(guess_number)
