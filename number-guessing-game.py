import random

print("NUMBER GUESSING GAME")
print("I'm thinking of a number between 1 and 100. You have 10 lives, goodluck!")

while True:
    num = random.randint(1, 100)
    lives = 10
    attempts = 1

    while lives > 0:
        try:
            guess = int(input(f"\nAttempt {attempts}/10. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!!")
            continue

        if guess > num:
            print("Try again, it's lower!")
            lives -= 1
            attempts += 1
            print(f"You have {lives} lives left")
        elif guess < num:
            print("Try again, it's higher!")
            lives -= 1
            attempts += 1
            print(f"You have {lives} lives left!")
        else:
            print(f"You got it right, in just {attempts} attempts!")
            break

    if lives == 0:
        print(f"Sorry, you're out of lives! The number was {num}")

    again = input("\nDo you want to play again? (y/n): ").lower().strip()
    if again.startswith("n"):
        break
