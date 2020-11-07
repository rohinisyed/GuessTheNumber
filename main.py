
# Guess the Number
#
# 1. Generate a Random Number between 1 and 100. This is the number that the player has to guess.
# 2. Ask the player to guess the number.
# 3. If the player guesses a number which is more than the random number, display : "Too High" and ask them to guess again
# 4. If the player guesses a number which is less than the random number, display : "Too Low" and ask them to guess again
# 5. If the player guesses the number correctly. Display that they won and ask them whether they want to play the game again


from random import randint 

play_game=True

random_number = randint(1,100)

while play_game:
  player_guess = int(input("Guess the number: "))
  if player_guess > random_number:
    print ("Too High, Try again!") 
  elif player_guess < random_number: 
    print ("Too low, Try Again!")
  else:
    play_again = input ("You won, Want to play again Y/N?:")   
    if play_again == "Y":
      random_number = randint(1,100)
    elif play_again == "N":
      play_game=False