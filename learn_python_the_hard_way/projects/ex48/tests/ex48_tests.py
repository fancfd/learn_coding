from nose.tools import *
from ex48 import lexicon

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
