AGENDA
=======
1. Questions?
2. Split into project groups
3. Work on projects for an hour?
4. Ask for four volunteers from different groups to present each project
5. Review existing code that uses these concepts in the [PyLadies Repo](https://github.com/PyLadies-Boston/PyLadies-Boston-Meetups/tree/master/Beginner/Round%201/2013-07-07) and in [Margaret's Repo](https://github.com/eudaimonious/data-formatting-tool)


# PROJECT 1

*Hint:* Check out [Chapter 17](http://learnpythonthehardway.org/book/ex17.html)

One: Ask user for file name

Two: Check to see if file exists

Three: If file currently exists, allow the user to cancel out
 
*Hint:*
	
	if exists(filename):
		your code here

Four:  Write some text in that file.

Five: *Extra Challenge:* Use string formatters


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
