import random

print("Hi there, what's your name")

playerName = input()

print(f"Hi {playerName}, I'm thinking of a number between 1 and 100.")
print('Try to guess my number.')

number = random.randint(1, 100)
attempts = 0
userGuess = int(input())
while number != userGuess:
    if userGuess < number:
        print('Your guess is too low, try again.')
        attempts += 1
        userGuess = int(input())
    elif userGuess > number:
        print('Your guess is too high, try again.')
        attempts += 1
        userGuess = int(input())
    else:
        print(
            f"Great job, {playerName}! You guessed my number in {attempts} tries!")
        break
