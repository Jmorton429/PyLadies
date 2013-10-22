# PROJECT 4
# Write a program (Python script) named madlib.py, which asks the user to enter a series of nouns, verbs, adjectives, adverbs, plural nouns, past tense verbs, etc., and then generates a paragraph which is syntactically correct but semantically ridiculous (see http://madlibs.org for examples).

adj1 = raw_input("Please enter an adjective: ")
plnoun1 = raw_input("Please enter a plural noun: ")
ffname = raw_input("Please enter a feminine first name: ")
lname = raw_input("Please enter a last name: ")
noun1 = raw_input("Please enter a noun: ")
place = raw_input("Please enter a place: ")
spevent = raw_input("Please enter a special event: ")
verb = raw_input("Please enter a verb: ")	
noun2 = raw_input("Please enter a noun: ")	
presverb = raw_input("Please enter a verb in the present tense: ")
noun3 = raw_input("Please enter a noun: ")	
noun4 = raw_input("Please enter a noun: ")	
noun5 = raw_input("Please enter a noun: ")	
noun6 = raw_input("Please enter a noun: ")
verb1 = raw_input("Please enter a verb: ")		

print """
Ah, look at all the %s %s!
Ah, look at all the %s %s!

%s %s picks up the %s in a %s where a %s has been.
%s in a %s.

%s at the %s, wearing the %s that she keeps in a %s by the %s. Who is it for?

All the %s %s, where do they all come from?
All the %s %s, where do they all %s?
""" % (adj1,plnoun1,adj1,plnoun1,ffname,lname,noun1,place,spevent,verb,noun2,presverb,noun3,noun4,noun5,noun6,adj1,plnoun1,adj1,plnoun1,verb1)