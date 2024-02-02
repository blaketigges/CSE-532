import random

def GISimple(impSpd = (1,9), golemSpd = (3,5), headStart = 5, exitPosition = 50):
    golem = 0
    imp = headStart

    play = True
    while play == True:
        if imp >= exitPosition:
            play = False
            return True
        elif golem >= imp:
            play = False
            return False
        imp += random.randint(impSpd[0], impSpd[1])
        golem += random.randint(golemSpd[0], golemSpd[1])
