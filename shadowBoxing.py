'''
this class will hold all the code for the game

Nicolas Turner 1.8.24
'''
from directionsEnum import directions
import random


up = directions.UP.value
down = directions.DOWN.value
left = directions.LEFT.value
right = directions.RIGHT.value

moveList = [up, down, left, right]
moves = ["up", "down", "left", "right"]
gameOver = False

'''
this method will be called when the computer is punching
'''
print("\nWelcome to Shadow Boxing! You'll be throwing punches first. \n")

def computerPunching(moveListString):
    global gameOver

    randomMove = random.randint(0,len(moveListString) - 1)

    print("Its my turn to punch.")
    firstMove = str(input("What is your first move (press and arrow key) ? ")).lower()
    if firstMove == moveListString[randomMove]:
        moveListString.pop(randomMove)
        randomMove = random.randint(0,len(moveListString) - 1)
    else:
        print(f"I moved {moveListString[randomMove]} \n")
        userPunching(moves)
    
    print("Nice one!")
    secondMove = str(input("What is your second move (press and arrow key) ? ")).lower()
    if secondMove == moveListString[randomMove]:
        moveListString.pop(randomMove)
        randomMove = random.randint(0,len(moveListString) - 1)
    else:
        print(f"Nice dodge! I moved {moveListString[randomMove]} \n")
        userPunching(moves)

    print("You're good at this!")
    finalMove = str(input("What is your final move (press and arrow key) ? ")).lower()
    if finalMove == moveListString[randomMove]:
        moveListString.pop(randomMove)
        print("You lose!")
        return print("You suck! Thanks for playing!")
    else:
        print(f"I almost got you! I moved {moveListString[randomMove]} \n")
        userPunching(moves)

'''
this method will be called when the user is punching
'''
def userPunching(moveListString):
    global gameOver

    randomMove = random.randint(0,len(moveListString) - 1)
    
    print("Its your turn to punch!")
    firstMove = str(input("What is your first move (press and arrow key) ? ")).lower()
    if firstMove == moveListString[randomMove]:
        print(f"I moved {moveListString[randomMove]} \n")
        moveListString.pop(randomMove)
        randomMove = random.randint(0,len(moveListString) - 1)
    else:
        print(f"I moved {moveListString[randomMove]} \n")
        computerPunching(moves)
    
    secondMove = str(input("What is your second move (press and arrow key) ? ")).lower()
    if secondMove == moveListString[randomMove]:
        print(f"I moved {moveListString[randomMove]} \n")
        moveListString.pop(randomMove)
        randomMove = random.randint(0,len(moveListString) - 1)
    else:
        print(f"Almost! I moved {moveListString[randomMove]}. \n")
        computerPunching(moves)
    
    finalMove = str(input("What is your final move (press and arrow key) ? ")).lower()
    if finalMove == moveListString[randomMove]:
        print(f"I moved {moveListString[randomMove]} \n")
        moveListString.pop(randomMove)
        randomMove = random.randint(0,len(moveListString) - 1)
        return print("Congrat you win! Thanks for playing!")
    else:
        print(f"So close! I moved {moveListString[randomMove]} \n")
        computerPunching(moves)

userPunching(moveList)
