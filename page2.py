#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page."""
"""
Name: James Anderson
Name of Project: Best 3 out of 5 Rock, Paper Scissors


#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import random

listofchoices = ['Rock', 'Paper', 'Scissors']

timestoplay = int(input("How many times would you like to play? Enter 1 for first to one and 3 for first to 3: "))

Pwins = 0 
Cwins = 0

while True:

  Computer = random.choice(listofchoices)

  Player = input("Choose: Rock, Paper, or Scissors: ")
  
  print(">>> You chose:", Player)
  print(">>> The computer chose:", Computer)

  if Player == Computer:
    print("It's a tie!")

  elif Player == 'Rock':

    if Computer == 'Scissors':
      print("Rock smashes the scissors! You win!")
      Pwins = Pwins + 1

    elif Computer == 'Paper':
      print("Ouch! Paper covers rock! You lose!")
      Cwins = Cwins + 1
  elif Player == 'Paper':

    if Computer == 'Rock':
      print("Paper covers rock! You win!")
      Pwins = Pwins + 1

    elif Computer == 'Scissors':
      print("Oof! Scissors cuts paper! You lose!")
      Cwins = Cwins + 1

  elif Player == 'Scissors':

    if Computer == 'Paper':
      print("Scissors cuts paper! You win!")
      Pwins = Pwins + 1

    elif Computer == 'Rock':
      print("Oh no! Rock smashes the scissors! You lose!")
      Cwins = Cwins + 1

  else: 
    print("That's not a valid input.")

  if Pwins == 3 or Cwins == 3:
    print("You won:", Pwins, "The computer won:", Cwins)

    if Pwins > Cwins:
      print("You win the game!")

    elif Cwins > Pwins:
      print("Dang you lost! Better luck next time!")
    break
"""
  

