from game_logic import GameLogic
import re

current_round = 0
total_score = 0
unbanked_score = 0
dice = 6
dice_rolled = str()
roll_score = 0
game_status = True
dice_saved = []
round_status = True


def play():

    # print(f'total_score: {total_score}')
    # print(f'Current Round: {current_round}')
    def intro():
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')

    def play_round():
        global total_score
        global current_round
        global unbanked_score
        global dice
        global dice_rolled
        global roll_score
        global game_status
        global dice_saved
        global round_status
        round_status = True
        current_round += 1
        unbanked_score = 0
        dice = 6
        print(f'Starting round {current_round}')
        while round_status is True:
            roll()
        if game_status is False:
            return

    def roll():
        global total_score
        global current_round
        global unbanked_score
        global dice
        global dice_rolled
        global roll_score
        global game_status
        global dice_saved
        global round_status
        print(f'Rolling {dice} dice...')
        # zero out the unbanked score
        # set dice to roll to 6
        # roll the dice
        dice_rolled = GameLogic.roll_dice(dice)
        # Format the string later
        dice_rolled_string = str(dice_rolled[0])
        if len(dice_rolled) >= 2:
            for di in range(1, len(dice_rolled)):
                dice_rolled_string += ', ' + str(dice_rolled[di])
        print(f'*** {dice_rolled_string} ***')
        roll_score = GameLogic.calculate_score(dice_rolled)
        # print(roll_score)
        # roll_score = 0
        if roll_score == 0:
            print(f"This round you've earned 0 points. Total score is {total_score}. Starting next round!")
            round_status = False
            return
        print('Enter dice to keep, or (q)uit:')
        user_input = input('> ')
        if user_input == 'q':
            print(f'Thanks for playing. You earned {total_score} points.')
            game_status = False
            round_status = False
            return
        # else dice to keep, adjust dice to roll and update unbanked points, roll then prompt
        user_input = string_to_list(user_input)
        user_dice_count = count_dice(user_input)
        rolled_dice_count = count_dice(dice_rolled)
        valid_data = True
        for di_value in range(1, 7):
            if user_dice_count[di_value] > rolled_dice_count[di_value] or len(user_input) == 0:
                valid_data = False
                print('Bad Input, Game Over!')
                game_status = False
                round_status = False
                return
        dice_saved = dice_saved + user_input
        dice -= len(user_input)
        roll_score = GameLogic.calculate_score(user_input)
        if roll_score == 0:
            round_status = False
        unbanked_score += roll_score
        print(f"You have {unbanked_score} unbanked points and {dice} dice remaining")
        print('(r)oll again, (b)ank your points or (q)uit:')
        user_input = input('> ')
        if user_input == 'q':
            print(f'Thanks for playing. You earned {total_score} points.')
            game_status = False
            round_status = False
            return
        if user_input == 'b':
            total_score += unbanked_score
            print(f'You banked {unbanked_score} points in round {current_round}')
            print(f'Total score is {total_score} points')
            round_status = False
            return
        if user_input == 'r':
            return

    def string_to_list(string_user_input):
        global dice_rolled
        s = ''.join(char for char in string_user_input if char.isdigit())
        output_list = [int(num) for num in s if num.isdigit()]
        return output_list

    def count_dice(dice_to_count):
        #input is going to be a list of dice
        #output is a list of counts for each result
        count = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        for die in dice_to_count:
            count[die] += 1
        return count





    intro()
    user_choice = input('> ')
    if user_choice == 'n':
        return print('OK. Maybe another time')
    # print(f'Total Score: {total_score}')
    # print(f'Current Round: {current_round}')
    while total_score < 500 and game_status is True:
        play_round()
    if total_score >= 500:
        print(f'Thanks for playing. You made it to 500 points!!')



if __name__ == '__main__':
    play()



