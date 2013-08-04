# Cave 1
"""The cave with the while unicorns"""
def cave1():

    print "There are unicorns playing harps"
    print "1. take picture-and post to facebook"
    print "2. pass out"
  
    unicorn = raw_input("> ")

    if unicorn == "1":
        print "no one buys it- your post is flagged"
    elif unicorn == "2":
        print "you hit your head on rocks - huge head ache"
    else:
       print "I said either 1 or 2"

    print "Now all the unicorns are leaving the cave"		
    unicorns = 10 
    while unicorns>0:
        print "unicorn number %d jumps out of cave" % unicorns
        unicorns = unicorns-1
		
    exit(0)
	
	
# Cave 2
"""The cave with the dictionary bars"""
def cave2():

    drinks = {
        'Meadhall': 'martini, shaken not stirred',
	    'Druid\'s': 'cold lonestar',
	    'Atwood\'s': 'tequila shot with a worm'
    }

    print "You chose the best cave, this is the cave with the bars!!!"
    print "Choose a bar to enter:"
    print "1. Meadhall"
    print "2. Druid's"
    print "3. Atwood's"

    choice = raw_input("> ")

    if choice == "1":
        print "Nice choice, have a %s" % drinks['Meadhall']
    elif choice == "2":
        print "Nice choice, have a %s" % drinks['Druid\'s']
    elif choice == "3":
        print "Nice choice, have a %s" % drinks['Atwood\'s']
    else:
        "I'll take it you don't want to drink tonight, goodbye!"

    exit(0)

	
# Cave3
"""The cave with the for drinks"""
def cave3():
    people = [1, 2, 3, 4, 5]
    drinks = ['', 'beer', 'wine', 'shakes', 'mojitos', 'margaritas']
    print "There is a waitress standing at the table."
    for number in people:
        print "Waitress: What would like to drink?\n1 Beer\n2 Wine\n3 Shakes\n4 Mojitos\n5 Margaritas\n"
        order = int(raw_input("> "))
        print "Your order is " + drinks[order] + ".\n\n"
    
    exit(0)
	
		
# Cave 4
"""The cave with Jennifer"""
def cave4():

    print "You find yourself facing Jennifer who asks if you've been practising your Python. What do you say?"
    print "1. Roll up LPTHW and hit yourself repeatedly until you pass out."
    print "2. Shout 'Django!' and run away."

    code = raw_input (" >")

    if code == "1":
        print "You wake up to find yourself shackled to Zed Shaw and become a Pythonista. Good job!"
    elif code == "2":
        print "You have to move to New York to join the PyLadies there. Head to South Station."
    else:
        print "Well, learning all about %s is probably a good idea." %code

    exit(0)
	

# Main		
print "You are on a mountain there are 4 caves here, you must pick one:"

while True:

    cave_number = raw_input("> ")

    if cave_number == "1":
        cave1();
    elif cave_number == "2":
        cave2();
    elif cave_number == "3":
        cave3();
    elif cave_number == "4":
        cave4();
    else: 
        print "Aren't 4 caves enough for you??"	