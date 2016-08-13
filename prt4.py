lowend = 1
highend = 100
guess = 50
choice = 0

print "Hello Barny!"
print "Please think of a number between 0-100."
print "Got it?"
print "Good."

print "Ok, first question is the number greater than or equal or less than 50"

#should i be doing "from random import randint"
#and is this how you wanted it to work or should I be coupling it a different way

while choice != 'c':
    print "Is your secret number " + str(guess) + "?"
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.",
    choice = raw_input("Enter 'c' to indicate I guessed correctly.")
    if choice == 'c':
        break
    elif choice == 'h':
            highend = guess
            guess = (highend + lowend)/2
            print 'Is your secret number ' + str(guess) + "?"
            choice = 0
    elif choice == 'l':
            lowend = guess + 1
            guess = (highend + lowend)/2
            print 'Is your secret number ' + str(guess) + "?"
    else:
            print "Sorry, I did not understand your input."
            choice = 0

print 'Your number is: ' + str(guess) + "."

#how should I add a counter for how many times is took to guess the correct number
