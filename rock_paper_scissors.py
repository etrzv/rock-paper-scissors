import random


def play_f():
    user_wins = 0
    computer_wins = 0
    random_number = random.randint(0, 2)      # rock = 0, paper = 1, scissors = 2
    options = ['rock', 'paper', 'scissors']

    while True:
        user_pick = input('Type rock/paper/scissors or q to quit: ').lower()
        if user_pick == 'q':
            print(f'You have won: {user_wins} times.')
            print(f'The computer has won: {computer_wins} times.')
            print('Goodbye!')
            exit()

        random_number = random.randint(0, 2)      # rock = 0, paper = 1, scissors = 2
        computer_pick = options[random_number]
        print(f'Computer picked: {computer_pick}.')

        if user_pick == 'rock' and computer_pick == 'scissors':
            print('You won!')
            user_wins += 1
        elif user_pick == 'paper' and computer_pick == 'rock':
            print('You won!')
            user_wins += 1
        elif user_pick == 'scissors' and computer_pick == 'paper':
            print('You won!')
            user_wins += 1
        elif user_pick == computer_pick:
            print('The game is draw.')
            continue
        else:
            print('You lost!')
            computer_wins += 1


play_f()
