print ("Guess a number between 1-100")
counts = 0
counts = counts +1
max = 101
min = 1

guess = (max-min)/2

while guess !=number:
	if number>guess:
		min=guess   
	elif number<guess:
		max =guess
	else
		print'Your number is' +str(guess)

	guess =(max-min)/2

print("That right! You got", counts, "count.")
