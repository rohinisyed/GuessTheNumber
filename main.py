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