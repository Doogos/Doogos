#!/usr/bin/env python
from random import randint
#Rock, Paper, Scissors
#create a list of play options
t = ["Rock", "Paper", "Scissors", "Dragon"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to true
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covered", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Dragon":
            print("You melt the computer")

    else:
        print("That's not how you play rock, paper, scissors!")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
