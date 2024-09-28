import random
def guess_the_number():
    low = 1
    high = 100
    attempts = 10

    number_to_guess = random.randint(low, high)
    print(f"Welcome to 'Guess the Number'!")
    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue


        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
guess_the_number()
