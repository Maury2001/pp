things ="one_piece aot berserk tokyo_ghoul"

print("they aren't ten")

stuff =things.split(' ')
more_stuff = ["Day", "Night", "song","corn","boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()

    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now" % len(stuff))

print("there you go:" , stuff)
print("some things with stuff")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))
