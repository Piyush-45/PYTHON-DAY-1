# ROCK PAPER SCISSORS
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# code goes here

# PRINTING IMAGES
game_images = [rock, paper, scissors]

user_input = int(input('What would you like to choose ? "Rock", "Paper", "Scissors" \n'))
print(game_images[user_input])

computer_input = random.randint(0,2)
print(f"compute chose: {computer_input} ")
print(game_images[computer_input])
if user_input == computer_input:
    print("MATHC DRAW...")
elif user_input == 0 and computer_input == 1:
    print("you lose")
elif user_input == 0 and computer_input == 2:
    print("you won")
elif user_input == 1 and computer_input == 0:
    print("You won")
elif user_input ==1 and computer_input == 2:
    print("you lose")
elif user_input == 2 and computer_input == 1:
    print("You won")
elif user_input== 2 and computer_input == 0:
    print("you lose")
else:
    print("wrong selection")
