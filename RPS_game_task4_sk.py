#This is Rock, Paper and Scissor game developed by Swetankan Kumar Sinha (Batch A28)

# importing Random Module 
import random

#All Function Defination
#main function
def game(computer_choice, user_choice):
  if computer_choice == user_choice:
    print("The game is a tie!")
  elif (computer_choice, user_choice) in (('r', 'p'), ('p', 's'), ('s', 'r')):
    print("You win!")
  else:
    print("You lose! Try again.")

# Function To convert user choice to a word
def convert_choice(choice):
  choices_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}
  try:
    return choices_dict[choice]
  except KeyError:
    raise ValueError("Invalid choice")

#Function To get user choice
def get_user_choice():
  while True:
    choice = input("Select among: Rock(r), Paper(p), Scissor(s): ").strip().lower()
    if choice in ['r', 'p', 's']:
      return choice
    else:
      print("Invalid input. Please enter 'r', 'p', or 's'.")

#Function to get computer choice
def get_computer_choice():
 return random.choice(['r', 'p', 's'])

#main
print("Welcome to the Rock Paper Scissors game!")

while True:
  try:
    computer_choice = get_computer_choice()
    print("Computer has chosen. Now your turn.")
    user_choice = get_user_choice()
    print(f"You chose {convert_choice(user_choice)}.")
    game(computer_choice, user_choice)
    print(f"Computer chose {convert_choice(computer_choice)}.")
  except ValueError as e:
    print(f"Error: {e}")

  play_again = input("Do you want to play again? (y/n): ").strip().lower()
  if play_again != "y":
    break

print("Thanks for playing!")
