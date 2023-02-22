import random

def guess_char():
    char = random.choice('abcdef')
    max_trials = 4
    for i in range(1, max_trials+1):
        guess = input("Enter your guess for the character between a and f: ")
        print(f"Your guess: {guess} (iteration {i}, trials left: {max_trials-i})")
        if guess == char:
            print(f"Congratulations! Your guess {guess} is the correct character.")
            return
    print(f"Sorry, you did not guess the correct character. The correct character was {char}.")

guess_char()
