import random

answer = False

selection = input("Would you like to play the Number Guessing Game? Y for yes / N for no ")

while selection == 'Y':
    number = random.randint(0,9)
    guesses = 0
    user_guess = int(input("Guess a number between 1 - 10: "))
    answer = False

    while answer == False:

        if user_guess == number:
            guesses += 1
            print("Congratulations! You answered correctly! ")
            print(f"Guesses: {guesses}")
            answer = True
        else:
            guesses+= 1 
            user_guess = int(input("Try again! :) Guess a number between 1 - 10: "))

    selection = input("Would you like to play the Number Guessing Game? Y for yes / N for no ")


    

