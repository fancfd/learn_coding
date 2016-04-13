def scan(line):

    list = line.split()

    map = []
    for i in list:
        key = find_key(i)
        if key:
            map.append((key, i))
    print map


def find_key(word):
    vocabulary = {
        'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        'verbs': ['go', 'stop', 'kill', 'eat']
    }
    for k in vocabulary:
        for val in vocabulary[k]:
            if word == val:
                return k
    return 'error'

if __name__ == '__main__':
    scan("Hello world this is east way, go up and down!")
