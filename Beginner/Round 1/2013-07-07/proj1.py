# PROJECT 1
# Ask user for file name
# Check to see if file exists
# if file currently exists, allow the user to cancel out
# define a function that takes in a file name and writes a file to that name. put whatever you want in the file.
# extra challenge: use string formatters
from os.path import exists

def write_to_file(filename):
	contents = raw_input("Please enter the text you want in the file, then press RETURN. ")
	out_file = open(filename, 'w')
	out_file.write(contents)

filename = raw_input("Please enter a file name. ")
print "Does %s currently exist? %r" % (filename,exists(filename))
raw_input("Press RETURN to continue, CTRL-C to abort.")
write_to_file(filename)