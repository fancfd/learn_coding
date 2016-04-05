# -*- coding: utf-8 -*-
name = '樊春·'
age = 39 # not a lie
height = 172 # inches
weight = 160 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d centimeter tall." % height
print "He's %d kilogram heavy." % weight 
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeath are usually %s depending on the coffee." % teeth

# this is tricky, try to get it exactly right
print "If I add %d, %d, and %d, and I get %d." % (
	age, height, weight,  age + height + weight)

