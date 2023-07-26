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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Invalid choice. Please choose 0, 1, or 2.")

choices = [rock, paper, scissors]
comp_choice = random.choice(choices)

print("The computer chose:")
print(comp_choice)

if comp_choice == choices[player_choice]:
    print("It's a draw!")
elif (comp_choice == rock and player_choice == 2) or (comp_choice == paper and player_choice == 0) or (comp_choice == scissors and player_choice == 1):
    print("You lose!")
else:
    print("You win!")
