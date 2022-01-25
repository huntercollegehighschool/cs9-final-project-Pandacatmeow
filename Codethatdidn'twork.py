def bestofone():
  if x == 1:
    if Player == Computer:
      print("It's a tie!")
      return 'Tie'
    elif Player == 'Rock':
      if Computer == 'Scissors':
        print("Rock smashes the scissors! You win!")
        return 'Win'
      elif Computer == 'Paper':
        print("Ouch! Paper covers rock! You lose!")
        return 'Lose'
    elif Player == 'Paper':
      if Computer == 'Rock':
        print("Paper covers rock! You win!")
        return 'Win'
      elif Computer == 'Scissors':
        print("Oof! Scissors cuts paper! You lose!")
        return 'Lose'
    elif Player == 'Scissors':
      if Computer == 'Paper':
        print("Scissors cuts paper! You win!")
        return 'Win'
      elif Computer == 'Rock':
        print("Oh no! Rock smashes the scissors! You lose!")
        'Lose'
    else: 
      print("You chose: An invalid input. Capitalize the first letter (Type either Rock, Paper, or Scissors)")

  def bestofthree():
  if x == 3:
    Cwins = 0
    Pwins = 0
    while Cwins < 3 and Pwins < 3:
      return bestofone()

----------------------------------------------------------------------------------------
import random

listofchoices = ['Rock', 'Paper', 'Scissors']

while True:
  try:
      timestoplay = int(input("Would you like to play best out of 3 or best out of 5? 3 for best out of 3 and 5 for best out of 5: "))
      if timestoplay == 3 or timestoplay == 5: 
        break
      else:
        print("That's not a valid input.")
        
neededwins = (timestoplay/2) + 1
Pwins = 0
Cwins = 0

while True:
  
    while True:
      Player = input("Choose: Rock, Paper, or Scissors: ")
      if Player == 'Rock' or Player == 'Paper' or Player == 'Scissors':
        break
    Computer = random.choice(listofchoices)
    print("You chose:", Player)
    print("The computer chose:", Computer)
    if Player == Computer:
      print("It's a tie!")
      pass
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
    if Pwins == neededwins or Cwins == neededwins:
      break

  if Pwins > Cwins
   print("You win! :D") 
  else:
    print("Dang! The computer beat you! Better luck next time!") 

    
      