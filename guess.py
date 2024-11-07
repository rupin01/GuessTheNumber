import random
import time

def play_game():
    number = random.randint(1, 200)
    name = input("May I ask you for your name? ")
    print(f"{name}, I'm thinking of a number between 1 and 200. Guess it!")

    guesses_taken = 0
    while guesses_taken < 6:
        try:
            guess = int(input("Guess: "))
            guesses_taken += 1

            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                break  # Correct guess

        except ValueError:
            print("Please enter a valid number.")

    if guess == number:
        print(f"Congratulations, {name}! You guessed the number in {guesses_taken} tries.")
    else:
        print(f"Sorry, the number I was thinking of was {number}.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break