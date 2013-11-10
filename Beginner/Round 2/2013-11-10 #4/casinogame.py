import random
from random import choice
from random import randint



def enter_casino():
	print "You just entered a casino with slots, blackjack, and a guessing game."
	game = raw_input("What would you like to play? ")
	if game == "slots":
		slot_machine()
	elif game == "blackjack":
		blackjack()
	elif game == "guessing game":
		start_guessing_game()
	else:
		FantasyCasino()
		

def slot_machine():
	fruits = ['apple', 'watermelon', 'strawberry', 'banana']
	
	index  = random.randint(0, 3)
	fruit1 = fruits[index]

	index  = random.randint(0, 3)
	fruit2 = fruits[index]

	index  = random.randint(0, 3)
	fruit3 = fruits[index]

	print fruit1 + ' / ' + fruit2 + ' / ' + fruit3
	if fruit1 == fruit2 == fruit3:
		print 'You won!!!'
	else:
		print 'Maybe next time'
		
def blackjack():
    deck = range(1,11)
    
    myCardsSum = 0      
    continuePlaying = 'y'
    
    while continuePlaying == 'y' and myCardsSum < 21:
        randomCard = choice(deck)
        deck.remove(randomCard) 
        myCardsSum += randomCard
        print 'You drew a ' + str(randomCard) + ', your sum is ' + str(myCardsSum) + '\n'
        if myCardsSum == 21:
            print 'Congratulations, you win'
            return
        elif myCardsSum > 21:
            print 'You are busted, you die a horrible death'
            return
        else:
            continuePlaying = raw_input('Do you want to draw another card? y/n \n')
         
    dealerSum = randint(1, 56)
    print 'Dealer drew a ' + str(dealerSum) + '\n'
    if dealerSum < myCardsSum:
        print 'You win'
    else:
        print 'Dealer wins'
        
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


def start_guessing_game():
	print "Welcome to the guessing game."
	number = input("Guess a number between 1 and 10.")
	guessing_game(7, number)
	
def FantasyCasino():
    print chr(27) + "[2J"
    print """"
    From outside, the Fantasy Casino looks like a tropical paradise. Lush greenery
    sprouts from the concrete and stretches, touching the clouds. You push aside
    the brambles and enter the large wooden doors. There are three types of slot 
    machines - a Fairy Themed Machine, a Ghost Themed Machine and an Aquatic
    Themed Machine - which one do you pick?

                              .-------.
                              |Jackpot|
                  ____________|_______|____________
                 |  __    __    ___  _____   __    |  
                 | / _\  / /   /___\/__   \ / _\   | 
                 | \ \  / /   //  //  / /\ \\ \  []|  
                 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
                 | \__/\____/\___/   \/     \__/ []|
                 |===_______===_______===_______===|
                 ||*|\_     |*| _____ |*|\_     |*||
                 ||*|| \ _  |*||     ||*|| \ _  |*||
                 ||*| \_(_) |*||*BAR*||*| \_(_) |*||
                 ||*| (_)   |*||_____||*| (_)   |*|| __
                 ||*|_______|*|_______|*|_______|*||(__)
                 |===_______===_______===_______===| ||
                 ||*| _____ |*|\_     |*|  ___  |*|| ||
                 ||*||     ||*|| \ _  |*| |_  | |*|| ||
                 ||*||*BAR*||*| \_(_) |*|  / /  |*|| ||
                 ||*||_____||*| (_)   |*| /_/   |*|| ||
                 ||*|_______|*|_______|*|_______|*||_//
                 |===_______===_______===_______===|_/
                 ||*|  ___  |*|   |   |*| _____ |*||
                 ||*| |_  | |*|  / \  |*||     ||*||
                 ||*|  / /  |*| /_ _\ |*||*BAR*||*||              
                 ||*| /_/   |*|   O   |*||_____||*||        
                 ||*|_______|*|_______|*|_______|*||
                 |===___________________________===|
                 |  /___________________________\  |
                 |   |                         |   |
                _|    \_______________________/    |_
               (_____________________________________)


    """
    theme = raw_input("Type fairy, ghost or aquatic.")
    if theme == "fairy":
        print chr(27) + "[2J"
        print """




            ___
   __     / ::.:\\                     You pull the lever, aha! Three fairies!
 /::::'-.|::::&&&&&                   Suddenly, you feel a tap tap on your
 |::::::.\\\\ .&&&&/ \\                 shoulder. Your eyes follow. A slender 
  \ ::..::\\\\:&&? <,(                stick? Looking up, that face... it's a 
   \ ::::. \\\\ &&  _/                wand... held by a fairy! She smiles and
  /::'.:::. \\\\&&.|.                 disappears in a poof. There is a pile of
  | ..:'-.- / )___\ \\                 bills where she once stood.
   \ :::   /./|))))) '
     '-..-'./ \ --| \\\\
          ||   ) .|  \\\\.
          |\  /___|   \_)
          |_)///|\\\\\\
             ||||\\\\\\'
              \  | |
             _.\ / /.__
          .-' \/ | |/  '-.
        / .  .(  | | .  .  \\
      _|_   .  \ | |   .   _|_
     /    '-.  #)|)|#  . -'   \\
    |   .    ##/ | |###    .   |
    |  . .  ####\|\|####  . .  |
     \___ .-'########## '-.___/
      |     .  *####*  .     |
       \  . . / . . .\  . .  /
        \    / .  .  .\  .  /
          '-( .    .  .)-.'
              ' ----- '
                / /
               / /
               ( (
                \ \\
                 \ \\
                  ) )
                  / /
"""
    if theme == "ghost":
        print chr(27) + "[2J"
        print """

           ,                           You pull the lever. Whoosh Whoosh WHOOSH!
        .--')                          You feel rushes of cold air all around you.
       /    /                          A THUD, on your chest knocks you down.
      |    /                           You sit there on the floor, trying to 
   /`.\   (_.'\\                       see something, anything that could have
   \          /                        pushed you down. The air has stilled. 
    '--. .---'                         Patting your pockets, you find them empty.
      ( " )
       '-'
                ,
                 \`-,      ,     =-
             .-._/   \_____)\\
            ("              / =-
             '-;   ,_____.-'       =-
              /__.'


       .-.
      ( " )
   /\_.' '._/\\
   |         |
    \       /
     \    /`
   (__)  /
   `.__.'
"""

enter_casino()