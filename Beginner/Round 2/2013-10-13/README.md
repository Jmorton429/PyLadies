LPTHW CHEATSHEET EXERCISES 10 - 20
=======
**10\. Escape Sequences:**
Use the backslash (\\) before a special character you need to print. Using %r will include your escape sequences (eg, \\ or \\t or \\n). Use triple quotes (''' or """) for multi-line strings. [Go to Chapter 10](http://learnpythonthehardway.org/book/ex10.html)


**11\. Raw Input:**
> print "How old are you?",

> age = raw_input()

> print "How tall are you?",

> height = raw_input()

> print "How much do you weigh?",

> weight = raw_input()

> print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
[Go to Chapter 11](http://learnpythonthehardway.org/book/ex11.html)


**12\. Prompting People:**
> age = raw_input("How old are you? ")

> height = raw_input("How tall are you? ")

> weight = raw_input("How much do you weigh? ")

> print "So, you're %r old, %r tall and %r heavy." % ( age, height, weight)

[Go to Chapter 12](http://learnpythonthehardway.org/book/ex12.html)


**13\. Parameters, Unpacking, Variables:**
Import argv from the module called sys. Argv stands for "argument variable." It is a variable that holds any arguments you include when you run your Python script from the command line. You can "unpack" argv, and other things, by assigning each of the arguments it contains to a variable.

>from sys import argv


>script, first, second, third = argv


>print "The script is called:", script

>print "Your first variable is:", first

>print "Your second variable is:", second

>print "Your third variable is:", third

[What is the difference between an argument and a paremeter?](http://stackoverflow.com/questions/3176310/difference-between-parameter-and-argument)

[Go to Chapter 13](http://learnpythonthehardway.org/book/ex13.html)


**14\. Passing a variable to raw_input:** When you start to repeat yourself, use a variable instead of raw text. If you want to change 
that text, you'll only need to do it in one place.

>prompt = '> '


>print "Do you like me %s?" % user_name

>likes = raw_input(prompt)


>print "Where do you live %s?" % user_name

>lives = raw_input(prompt)


>print "What kind of computer do you have?"

>computer = raw_input(prompt)

[Go to Chapter 14](http://learnpythonthehardway.org/book/ex14.html)


**15\. Reading Files:** Create a new variable assignment (eg, "txt") and pass a filename to the "open" function. Then apply the ".read()" method, which uses "dot notation."

>txt = open(filename)


>print txt.read()

[Go to Chapter 15](http://learnpythonthehardway.org/book/ex15.html)

**16\. Working with Files:** Use open as in chapter 15 but pass it a second argument, "w", to open the file in write mode.
>text = open(filename, 'w')

You can also use dot notation to:

close -- Closes the file. Like File->Save.. in your editor.

read -- Reads the contents of the file. You can assign the result to a variable.

readline -- Reads just one line of a text file.

truncate -- Empties the file. Watch out if you care about the file.

write(stuff) -- Writes stuff to the file.

Example using readline on a file (filename) that only contains two lines of text.
> \>\>\> filename.readline()

>'This is the first line of the file.\n'

> \>\>\> filename.readline()

>'Second line of the file\n'

> \>\>\> f.readline()

> ''

[Go to Chapter 16](http://learnpythonthehardway.org/book/ex16.html)





