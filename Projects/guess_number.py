import random

#Asking the user to put the number range to guess.
top_of_range = input("Enter your number: ")

if top_of_range.startswith("-"):
    print("Please type a positive number next time.")
elif int(top_of_range) <= 0:
    print("Please type a number larger than 0 next time.")
    quit()
elif int(top_of_range) > 0:
    top_of_range = int(top_of_range)
    print("Now, Let's play your game!")

    random = random.randint(0, top_of_range)

    guess = 0
    while True:
        guess += 1
        user_guess = input("Guess the number: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == random:
                print("You got it!")
                break
            elif user_guess > random:
                print("Your number is above the number.")
                continue
            elif user_guess < random:
                print("Your number is below the number.")
                continue
        else:
            print("Please type a number next time.")
            continue
    print("You try it", guess, "times.")
else:
    print("Please type a number larger than 0 next time.")