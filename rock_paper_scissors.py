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

#Write your code below this line 👇
import random

# list_of_choices = [rock, paper, scissors]

# computer_rock = ['draw', 'you win', 'computer win']
# computer_paper = ['computer win', 'you win', 'you win']
# computer_scissors = ['you win', 'computer win', 'draw']
# victory_chart = [computer_rock, computer_paper, computer_scissors]

# computer_choice = random.randint(0,2)
# user_choice = input("The computer has challenged you to a game of rock, paper, scissors. The computer has made their choice. What is yours? Type 0 for rock, 1 for paper, or 2 for scissors.\n")

# print(f"Your Choice: \n {list_of_choices[int(user_choice)]}\n The computer's choice: {list_of_choices[int(computer_choice)]} \n {victory_chart[int(computer_choice)][int(user_choice)]}")

#### choice 2: if else
game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_image[computer_choice])

if user_choice >=3 or user_choice < 0:
    print('You typed an invalid number')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif user_choice == 2 and computer_choice == 0:
    print('You lose!')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif computer_choice == user_choice:
    print('draw')
