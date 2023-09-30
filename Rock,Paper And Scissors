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
import random
image=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(image[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(image[computer_choice])
if user_choice==0 and computer_choice==2:
  print("You Win!")
elif computer_choice>user_choice:
  print("You Lose")
elif user_choice>computer_choice:
  print("You Win!")
elif user_choice==computer_choice:
  print("It's a draw")
elif user_choice>=3 or user_choice<0:
  print("You entered an invalid number, You Lose")
  
