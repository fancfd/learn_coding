def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(stuff):
    """Sorts ths words."""
    return sorted(stuff)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentece(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Print the first and the last words of the sorted sentence."""
    words = sort_sentece(sentence)
    print_first_word(words)
    print_last_word(words)
