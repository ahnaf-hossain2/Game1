# game 1: Snake Water Gun Game
'''
We all have played snake water gun game in our childhood. If you haven't, google the
rules of this game and write a python program capable of playing this game with the
user.
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([-1, 0, 1])
yourChoice = input("Enter your choice: ").lower()
choiceDict = {
    "s": 1,
    "w": -1,
    "g": 0
}
# creating the reverse dictionary to get the value of the key entered by the user
# if user gives s then choiceDict["s"] will give 1 then reverseDict[1] will give "snake" output.
# using this to make the game output more user friendly
reverseDict = {
    1 : "snake",
    -1 : "water",
    0 : "gun"
}
you = choiceDict[yourChoice] # it will give the value of the key entered by the user for example if user enters "s" it will give 1 which is an integer
# below two lines are just for a nice output to show the choices of the computer and the user
# it is not related to the main logic of the game
print(f"Computer's choice: {reverseDict[computer]}")
print(f"Your choice: {reverseDict[you]}")

if you == computer:
    print("It's a tie")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("You lose!")
