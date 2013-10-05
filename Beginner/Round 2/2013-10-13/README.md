LPTHW CHEATSHEET EXERCISES 10 - 20
=======
**10\. Escape Sequences:**
Use the backslash (\\) before a special character you need to print. Using %r will include your escape sequences (eg, \\ or \\t or \\n). Use triple quotes for multi-line strings. [Go to Chapter 10](http://learnpythonthehardway.org/book/ex10.html)


**11\. Raw Input:**
> print "How old are you?",

> age = raw_input()

> print "How tall are you?",

> height = raw_input()

> print "How much do you weigh?",

> weight = raw_input()

> print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
