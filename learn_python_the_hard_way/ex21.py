def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def devide(a, b):
    print "DEVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some lath with just functions!"

age = add(30, 5)
height = substract(78, 5)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, substract(height, multiply(weight, devide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
