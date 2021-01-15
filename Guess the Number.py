import random

print("Hello! What is your name?")
name = input()

secret_no = random.randint(1, 10)
guess_rem = 5

print("Welcome " + name + ", I have a game for you. It\'s called \"Guess the Number\"")
print("I'm thinking of a number between 1 and 10. You have " + str(guess_rem) + " guesses.")

for guess_taken in range(5):
    print("Take a guess.")
    guess = int(input())
    guess_rem -= 1
    if guess < secret_no:
        print("Your guess is too low. You have " + str(guess_rem) + " remaining.")

    elif guess >secret_no :
        print("Your guess is too high. You have " + str(guess_rem) + " remaining.")

    else:
        break                                       #This is if the guess is correct

if secret_no == guess:
            print("Good job. You took " + str(guess_taken) + " guesses to find out the no.")
else:
    print("The number I was thinking of is " + str(secret_no) + '.')
