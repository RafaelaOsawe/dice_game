
f = open("player_score.txt", "a")

import random

total_rounds = 5
total_players = 2

print("Welcome to Dice 101!")
print()
print("There are 5 rounds in each game. In each round, each player rolls the two dice.")
print()
#1) Allows two players to enter their details, which are then authenticated to ensure that they are authorised players.

print("Player 1 please enter your name: ")
player1_name = input()
print("Please enter your age: ")
player1_age = int(input())
print()
print("Player 2 please enter your name: ")
player2_name = input()
print("Please enter your age: ")
player2_age = int(input())

if player1_age >= 18 and player2_age >= 18:
  print("Congratulations, you meet the requiremnetns to proceed in the game.")
  print()
elif player1_age <= 18 and player2_age <= 18:
  print("Sorry you are unable to play this game.")
else:
  print("Sorry you are unable to play this game.")
  quit()

#2) Allows each player to roll two 6-sided dice.

def dice_roll ():
  print("Please press enter to roll the dice.")
  enter = input()
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  total = roll1 + roll2
  return roll1, roll2
  print("You rolled a ",roll1, " and a ", roll2,". Totalling to ", total, " in round 1.")

newScore1, newScore2 = dice_roll()
print(newScore1, " + ", newScore2)
print(dice_roll)

#3) Calculates and outputs the points for each round and each player’s total score.
player1_total = 0
player2_total = 0
round = 0+1
#4) Allows the players to play 5 rounds.

for x in range(6):
  print("Round ",round, ": Player 1 please roll the dice")
enter = input()

newScore1, newScore2 = dice_roll()
print(newScore1, " + ", newScore2)
print(dice_roll)
player1_total = newScore1 + newScore2

print("Round 1: Player 2 please roll the dice")
enter = input()

newScore1, newScore2 = dice_roll()
print(newScore1, " + ", newScore2)
print(dice_roll)
player2_total = newScore1 + newScore2

#5) If both players have the same score after 5 rounds, allows each player to roll 1 die each until someone wins.

if player1_total == player2_total:
  print("Score tied. This is sudden death!")
  print("Player 1 please roll the dice.")
  newScore1, newScore2 = dice_roll()
  print(newScore1, " + ", newScore2)
  print(dice_roll)
  player1_total = newScore1 + newScore2
  print("Player 2 please roll the dice.")
  newScore1, newScore2 = dice_roll()
  print(newScore1, " + ", newScore2)
  print(dice_roll)
  player2_total = newScore1 + newScore2
if player1_total > player2_total:
    print("Congratulations, player 1 you win!")
elif player2_total > player1_total:
    print("Congratulations, player 2 you win!")

f.close()
#6) Outputs who has won at the end of the 5 rounds.

#7) Stores the winner’s score, and their name, in an external file.

#8) Displays the score and player name of the top 5 winning scores from the external file.