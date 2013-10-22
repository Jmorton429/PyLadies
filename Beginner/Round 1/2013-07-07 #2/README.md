AGENDA
=======
1. Questions?
2. Split into project groups
3. Work on projects for an hour?
4. Ask for four volunteers from different groups to present each project
5. Review existing code that uses these concepts (code in this repo and at https://github.com/eudaimonious/data-formatting-tool)


# PROJECT 1
1. Ask user for file name
2. Check to see if file exists
3. If file currently exists, allow the user to cancel out
4. Define a function that takes in a file name and writes a file to that name. Put whatever you want in the file.<br />
5. *Extra Challenge:* Use string formatters


# PROJECT 2
1. Fill in the body of the function definition for cat_n_times so that it will print the string, s, n times:
 
	def cat_n_times(s, n):<br />
		\<fill in your code here\>

2. Save this function in a script named import_test.py. Now at a unix prompt, make sure you are in the same directory where the import_test.py is located ( ls should show import_test.py). Start a Python shell and try the following:
 
	\>\>\> from import_test import *<br />
	\>\>\> cat_n_times('Spam', 7)<br />
	SpamSpamSpamSpamSpamSpamSpam

If all is well, your session should work the same as this one. Experiment with other calls to cat_n_times until you feel comfortable with how it works.


# PROJECT 3
1. Create function hotelCost that takes in number of days and nightly rate and returns the pre-tax total cost.
2. Create getTax function that takes pre-tax total and a tax rate and returns the grand total.

# PROJECT 4
Write a program (Python script) named madlib.py, which asks the user to enter a series of nouns, verbs, adjectives, adverbs, plural nouns, past tense verbs, etc., and then generates a paragraph which is syntactically correct but semantically ridiculous (see http://madlibs.org for examples).
