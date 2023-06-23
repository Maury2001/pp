def add (a,b):
    print("adding %d - %d " % (a,b))
    return a+b 

def subtract(a,b):
    print("subtracting %d -%d" %(a,b))
    return (a-b)

def divide(a,b):
    print("dividing %d /%d" %(a,b))
    return a/b

def multiply(a,b):
    print("multiplying %d *%d" %(a,b))
    return a*b
 

print("lets do math motherfuckeer with functions")
age = add(30,5)
height = subtract(78,4)
weight = multiply(5,5)
iq= divide(140,2)

print("age: %d \nheight: %d \nweight: %d \niq: %d" % (age, height, weight, iq))

print("this is supposed to be a puzzle but ofc you'll figure it out")

what= add(age, subtract(height, multiply(weight,divide(iq ,2))))

print("answer", what, "\nit wasn't even hard")

