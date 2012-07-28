from sys import argv

# grab name of file to open
script, filename = argv

# get a filehandle
txt = open(filename)

# print the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# get filename from direct user input
print "Type the filename again:"
file_again = raw_input("> ")

# get a filehandle
txt_again = open(file_again)

# print the contents of the file
print txt_again.read()

# be a good citizen - close file handles
txt.close()
txt_again.close()