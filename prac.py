from sys import argv 

# script , filename = argv

# txt = open(filename)

# print("ladies and gentlemen, your file \n %r" % filename)
# print(txt.read())

script , username = argv 

prompt='>'

print("hello %s" % username)
print("answer the following questions truthfully")
print("ass or boobs")
answer = input(prompt)

if answer == "boobs":
    print("still have a long way to go")
elif answer == "ass":
    print("Noiiice!!")    
    