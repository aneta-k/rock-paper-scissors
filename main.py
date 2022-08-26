import random

choices = ['Rock', 'Paper', 'Scissors']

user_points = 0
computer_points = 0

while True:
    user_choice = input('Rock, Paper or Scissors? (q - to quite the game): ').capitalize()
    if user_choice == 'Q':
        break
    if user_choice not in choices:
        print('You can choose only between Rock, Paper and Scissors. Try again!')
        continue
    
    computer_choice = random.choice(choices)
    print(f'Computer: {computer_choice}')
    
    if user_choice == computer_choice:
        print('It\'s a tie.')
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print('You get a point.')
        user_points += 1
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print('You get a point.')
        user_points += 1
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print('You get a point.')
        user_points += 1
    else:
        print('Computer geta point.')
        computer_points += 1

    print(f'User points: {user_points}\nComputer points: {computer_points}')
    
if user_points > computer_points:
    print('You won this game!')
elif user_points < computer_points:
    print('Computer won this game!')
else:
    print('It was a tie.')
    
print('Goodbye!')
# jak tu byłem znowu!!!