import random
import string

trials = 0
rand_letter = random.choice(string.ascii_lowercase)
print("Guess the letter in three tries!")

while trials < 3:
    letter_guess = input("Guess: ").lower()
    if letter_guess == rand_letter:
        print("You win!")
        break
    else:
        trials += 1
        if trials == 3:
            print("You lost.")
        else:
            print("Oops! That's incorrect. Try again!")