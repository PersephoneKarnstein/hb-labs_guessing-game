"""A number-guessing game."""
from math import log
import random, subprocess, time

global highscores, successful
highscores = [["NAME", "SCORE", "BEST POSSIBLE", "FRACTION"]]

yourname = input("Hello! What's your name? \n")

guess = 0
num_guesses = 0
guesses_bottom = int(input(f"Hi, {yourname}, what is the lower bound you want to guess from? "))
guesses_top = int(input("and the upper? "))
random_number = random.randint(guesses_bottom,guesses_top)
log2guesses = int((log(guesses_top-guesses_bottom)/log(2.))+1)
max_guesses = log2guesses+2 

successful = False

print(f"{yourname}, I'm thinking of a number from {guesses_bottom} to {guesses_top}. It should take you about {str(max_guesses-2)} guesses.")


##main game##
def guessinggame(guess, num_guesses, random_number, guesses_bottom=0, guesses_top=100):
    global successful, highscores
    if num_guesses <= max_guesses and guess !=random_number:
        num_guesses +=1

        if guess<guesses_bottom or guess>guesses_top:
            print("no! bad!")
            return [None, num_guesses, random_number]

        elif guess < random_number:
            print("Too low, guess again! ")
            return [-1, num_guesses, random_number]

        elif guess > random_number:
            print("Too high, guess again! ")
            return [+1, num_guesses, random_number]

    elif guess == random_number:
            print("congratulations, you guessed it in " + str(num_guesses) + " tries!")
            highscores.append([yourname, str(num_guesses), log2guesses, num_guesses/log2guesses])
            successful = True    
    else:
        print("you are very bad at guessing.")
        highscores.append([yourname, "disqualified", log2guesses, None])
        

##the computer part
def gocomp():
    global successful    # guessisint = False
    too_high = [guesses_top]
    too_low = [guesses_bottom]
    compared2answer = [99, num_guesses, random_number]
    print(f"hint, the answer is {random_number}")

    while successful == False:
        if compared2answer[0] == 99:
            pass
        elif compared2answer[0] == -1:
            too_low.append(guess)
        elif compared2answer[0] == +1:
            too_high.append(guess)
        
        guess = int((min(too_high) + max(too_low))/2.)
        
        # time.sleep(1)
        print(f"I guess {guess}!")
        compared2answer = guessinggame(guess, compared2answer[1], compared2answer[2], guesses_bottom=guesses_bottom, guesses_top=guesses_top)




gocomp()
# ##alternate with the computer##
# def multiplayer():
#  while successful == False:
#     guessinggame(guess )

#     for score in highscores: print(score)
#     again = input("would you like to play again? (Y/N): ")
#     if again.upper() == "Y":
#         continue
#     elif again.upper() == "N":
#         playcomp = input("would you like me to play? (Y/N): ")
#         if playcomp.upper() == "Y":
#             yourname = "computer"
#             gocomp()
#         else:
#             print("thanks for playing!")
#             break
#     else: 
#         print("huh? I think you should play again")
        # continue
    # Put your code here

