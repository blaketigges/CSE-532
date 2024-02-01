import random

impSpd = (1,9)
golemSpd = (3,5)
headStart = 5
exitPosition = 50
tunnels = []

def GISimple(impSpd, golemSpd, headStart, exitPosition):
    print(impSpd, golemSpd, headStart, exitPosition)
    for i in range(exitPosition):
        tunnels.append('-')
    tunnels.append('X')
    golem = 0
    imp = headStart
    # G----I--------------------------------------------X
    secs = 0
    play = True
    while play == True:
        for num, spot in enumerate(tunnels):
            if num == golem:
                print('G', end="")
            elif num == imp:
                print('I', end="")
            print(spot, end="")
        print("\t"+str(secs)+"s")
        secs += 1
        if imp >= exitPosition:
            print("Imp has escaped!")
            play = False
            return True
        elif golem >= imp:
            print("Golem has caught the imp!")
            play = False
            return False
        imp += random.randint(impSpd[0], impSpd[1])
        golem += random.randint(golemSpd[0], golemSpd[1])

def getInput():
    iMin = input("Enter the Imp's min speed: ")
    iMax = input("Enter the Imp's max speed: ")
    impSpd = (int(iMin), int(iMax))
    gMin = input("Enter the Golem's min speed: ")
    gMax = input("Enter the Golem's max speed: ")
    golemSpd = (int(gMin), int(gMax))
    headStart = int(input("Enter the Imp's head start: "))
    exitPosition = int(input("Enter the exit position: "))
    return impSpd, golemSpd, headStart, exitPosition

def main():
    impSpd, golemSpd, headStart, exitPosition = getInput()
    print(impSpd, golemSpd, headStart, exitPosition)
    GISimple(impSpd, golemSpd, headStart, exitPosition)