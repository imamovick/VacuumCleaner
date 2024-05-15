from vacuum import *
import random

directions = ['north', 'south', 'east', 'west']


def reflex_agent(percept):
    if percept:
        return 'clean'
    else:
        return 'north'


def random_agent(percept):
    if percept:
        return 'clean'
    else:
        return random.choice(directions)


last = 0


def state_agent(percept):
    global last
    x = 0
    # Keeping track of opposite directions:
    back = {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }

    if percept:
        return 'clean'
    else:
        while x == 0:
            y = random.randrange(0, 4)
            # Instructions not to go back to the last space
            if back[last] != y:
                x = 1
                # Remembering the last move
                last = y
                if y == 0:
                    return 'north'
                if y == 1:
                    return 'east'
                if y == 2:
                    return 'south'
                if y == 3:
                    return 'west'


#run(20, 50000, state_agent)
print(many_runs(20, 50000, 10, state_agent))
