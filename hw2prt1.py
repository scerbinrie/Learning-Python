#down vote
#favorite
#I wrote this script but it always returns the same answer ("Your guess is too high"), no matter what the user inputs. Any insight would be helpful.
#wrong idea

import random

number = random.randint(1, 10) 

guess = input("Guess a number between 1 and 10: ")

if type(guess == int):
    print(number) # this prints the randint to show the code isn't working

    while(number != 0):
        if(guess > number):
            print("Your guess is too high!")
            break

        elif(guess < number):
            print("That's too low.")
            break

        elif(guess == number):
            print("Thats's right!")
            break

    else:
        print("Please enter a number.")