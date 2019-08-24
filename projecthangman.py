# Hangman Game Project 2
import time
import os

word=input("Player1, Please enter the word to be guessed :")
print(word)
os.system('cls||clear')

length=len(word)
print("The Word Length is ", length)
guestlist=[]
turn=0
fail=0
"""Created this variable to check the correct and unique inputs from the
            user comparing it with the words length"""

turk=0
maxturn=length*2
maxfail=5+(length-2)
print("Please be noted that no Empty spaces should be entered or else game will be ended")
while (True):
    turn+=1
    print("=====Turn No=====",str(turn)+" ================")
#Ask the Player 2 for the Input
    guess=input("Guess the Word Player 2: ")

    # Handling the Space Error Exiting the Loops
    if (guess=="" or guess==" " or len(guess)>1):
        print("No Empty, No Extra Spaces, No more than 1 Character is required")
        break

    if guess in word:

        # Feedback is returned if the guess made is correct
        print("FeedBack : Correct Guess")

        # Handling the duplicate data
        if guess in guestlist:
            print("duplicate data")
        else:
        # turk is just a random variable plays a key role in the program
            turk+=1
            guestlist.append(guess)
            if (turk==length):
                print("Player Win")
                break

    else:
        # Trying again if the Word is not found or the guess is Wrong.
        print("FeedBack : Wrong Guess")

        fail+=1
        # Maintaning the Max Turn and Max Fail
    if (turn==maxturn or fail==maxfail):
        print("Turn or Failed Count Maxed Out")
        print("Player Losses")
        break

    print("Turn Left",maxturn-turn)

    print("Failed Attempts Remaining",maxfail-fail)
