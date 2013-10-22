def katie():

    guilt_count = 0
    while guilt_count < 2:
        kitten_status = "definitely_alive"

    
        kitten_answer = raw_input("""You see the CIC in front of you. There it is! So beautiful.\ 
    But, oh no! You see a stray kitten looking very scared of all the big cars.\ 
    Do you want to try to catch it? Yes or No?""")
        if kitten_answer == "No":
            guilt_count = guilt_count+1
            kitten_certainty = raw_input("Do you really want to leave this kitten? Yes or No?")
            if kitten_certainty == "Yes":
                guilt_count = guilt_count+1
                break
            else:
                print """Good call. You hop off your bike and swoop in to grab the kitten.\ 
Perhaps at PyLadies you can generate a robot that takes care of kittens.\ 
Time to get back on your bike and make it there!"""
                break
        else:
            print """Good call. You hop off your bike and swoop in to grab the kitten.\
Perhaps at PyLadies you can generate a robot that takes care of kittens.\
Time to get back on your bike and make it there!"""
            break
    
    
    coffee_answer = raw_input("""Onward, then. You see Au bon pain across the street from the CIC and think,\ 
'Maybe I should bike to ABP to get some coffee.' Would you like to get some coffee? Yes or No?""")
    if coffee_answer == "Yes" and kitten_status != "definitely_alive":
        print "Seriously, you'll stop for coffee but not the kitten? You are done with this game."
    exit()
    elif coffee_answer == "Yes" and kitten_status == "definitely_alive":
        print "Yum, delicious coffee. With your newfound caffeine-energy you race to PyLadies, kitten in tow."
    elif coffee_answer == "No" and kitten_status == "definitely_alive":
        print """That's right, no time for coffee, you've got a kitten to save with Python. You lock up your bike and head into the CIC."""
    


def panhandler():
	print "On your way out of South Station, you encounter a particularly nasty \
panhandler. \"Give me  money!\" he says, and refuses to get out of your way. What do you do?"
	print "1. Give him money"
	print "2. Try to push him away"
	panh = raw_input("> ")
	if panh == "1":
		print "How much? Enter number of dollars"
		money = 0
		contribution = int(raw_input("> "))
		money = money + contribution 
			
		while money <= 50:
			print "Gimme more!"
			contribution = int(raw_input("> "))
			money = money + contribution 
			
	elif panh == "2":
		print "You attempt to push him, but this guy is suprirsingly strong.\
\"Give me money!\" he says even more loudly. How much do you want to give him? Enter number of dollars"
		money = 0
		contribution = int(raw_input("> "))
		money = money + contribution 
			
		while money <= 50:
			print "Gimme more!"
			contribution = int(raw_input("> "))
			money = money + contribution 

	else:
		print "I don't understand what that means. Please type 1 or 2."

def driver():
	print "You bike over the Charlestown Bridge, and watch the sailors on the Charles River. \
A mean taxi driver cuts you off! \"Learn to ride a bike!\" he shouts, and honks his horn. \
What is your response?"
	print "1. Shut back, \"learn to follow basic traffic rules!"
	print "2. Ignore him and keep riding."
	driver = raw_input("> ")
	if driver == "1":
		print "Wow, that's brave. The taxi driver honks his horn angrily, but doesn't \
do anything else. You continue on to Cambridge Innovation Center."

	elif driver == "2":
		print "Way to take the high road. He looked pretty scary, anyways. \
You continue on to Cambridge Innovation Center."

	else:
		print "I don't understand what that means. Please type 1 or 2."
def avanti():
    print "Sorry"

if street == "Boylston Street":
    avanti()

elif street == "Summer Street":
    panhandler()
    driver()
    
elif street == "Amherst Street":
    katie()