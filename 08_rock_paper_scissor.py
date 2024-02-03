import random

def play_game():
    try:
        counter = 0
        computer_won = 0
        user_won = 0
        number_turns = int(input("How many turns do you want to play: "))
        
        choices = ['r','p','s']
        computer_choice = random.choice(choices)
        while counter < number_turns :
            my_choice = (input('Enter your choice (Rock(r),Paper(p),Scissor(s)): ').lower())
            if my_choice not in choices:
                raise ValueError('You can only enter rock, paper, or scissor.')
            elif (my_choice == 'r' and computer_choice == 'p') or \
                (my_choice == 'p' and computer_choice == 's') or \
                (my_choice == 's' and computer_choice == 'r'):
                print('Sorry, you lose.')
                computer_won += 1
            elif (my_choice == 'r' and computer_choice == 's') or \
                (my_choice == 'p' and computer_choice == 'r') or \
                (my_choice == 's' and computer_choice == 'p'):
                print('Congratulations! You won.')
                user_won += 1
            else:
                print('It\'s a tie!')
                
            counter+=1
        
        print(f'Your score:{user_won} | Computer score: {computer_won}')
        if computer_won > user_won:
            print ('Computer wins this round.')
        elif computer_won < user_won:
            print('Congratulations you won this round.')
        else:
            print("Its a tie.")
            
    except ValueError as ve:
        print(ve)

play_game()
    
while (input('Do you want to play again (Yes or No):').lower()=='yes'):
    play_game()