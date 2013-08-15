# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
    	name = "rock"
    elif number == 1:
    	name = "Spock"
    elif number == 2:
    	name = "paper"
    elif number == 3:
    	name = "lizard"
    elif number == 4:
    	name = "scissors"
    else:
    	name = None
    return name
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
        # don't forget to return the result!
    if name == "rock":
    	number = 0
    elif name == "Spock":
    	number = 1
    elif name == "paper":
    	number = 2
    elif name == "lizard":
    	number = 3
    elif name == "scissors":
    	number = 4
    else:
    	number = None
    return number

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    print "Player chooses %s." % name
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0,5,1)
    # convert comp_number to name using number_to_name
    computer_name = number_to_name(computer_number)
    print "Computer chooses %s." % computer_name
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - computer_number) % 5
    # use if/elif/else to determine winner
	# print results
    if diff == 0:
        print "Player and computer tie!"
        print " "
    elif (diff == 1) | (diff == 2):
        print "Player wins!"
        print " "
    elif (diff == 3) | (diff == 4):
        print "Computer wins!"
        print " "
    else:
        print "Looks like there's been an error."
        print " "

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


