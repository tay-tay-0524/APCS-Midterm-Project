#import random function for the user if they want computer to pick game
import random

#different files hold different games, so import tne function from the file
from change_text_game import change_text
from dice_game import rolling_dice
from eight_ball_game import game_of_8_ball


#intro into the game!

print("Welcome to the Game Choosing Game!")
print("For this game, we choose out of 2 games to play! Either a dice game or a 8 ball game! or the computer chooses!")
num = 1
options = ["Dice Game", "Magic 8 Ball", "Text to Binary Code", "Computer Chooses!"]
for i in options:
    print(f"{num}. {i}")
    num += 1


#in case they choose the computer to choose
numbers = random.randint(1,3)

#the choosing process
print("do you want to choose or the computer to choose?")
answer = input(" Answer > y/n > ")

if answer == "y":
    number = int(input("Enter number: "))
    if number == 1:
        change_text()
    elif number == 2:
        rolling_dice()
    elif number == 3:
        game_of_8_ball()

else: #if they let the computer else statement
    if numbers == 1:
        change_text()
    elif numbers == 2:
        rolling_dice()
    elif numbers == 3:
        game_of_8_ball()
