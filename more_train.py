from sys import argv

script, user_name = argv
prompt ='>'

print ("hi %s im the %s script" % (user_name, script))
print(" i'd like to ask you a few questions")
print("do you like me %s" % user_name)
likes = input(prompt)

print("where do you live %s" % user_name)
lives = input(prompt)

print("what kind of computer do you have ")
computer = input(prompt)

print (""" 
alright so you have said %r about liking me.
you live in %r . not sure where that is.
and you have a %r computer . nice
""" % (likes, lives, computer))