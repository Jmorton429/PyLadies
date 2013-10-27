def guessing_game(lucky_number, number):
	
	print "You guessed %d." % number
	
	if number == lucky_number:
		print "You win 1,000,000 dollars!"
	elif number > 7: 
		print "You lose. Too high."
	elif number < 7:
		print "You lose. Too low."
	else:
		print "You lose. You didn't follow the directions."

print "Welcome to the guessing game."
number = input("Guess a number between 1 and 10.")
guessing_game(7, number)