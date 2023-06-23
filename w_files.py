from sys import argv

script, filename =argv

print("we're going to erase %r" % filename)
print ("If you don't want that, hit CTRL- C (^C).")
print ("If you do want that, hit RETURN.")

input(">")
print("open file ...")
target = open(filename, "w")
print("truncating file . goodbye")
target.truncate()

print("now im going to ask you for three lines")

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print ("im going to write these to the file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("finally we close it")
target.close()

