if __name__ == "__main__":
    from game_logic import GameLogic
else:
    import sys
    sys.path.append('../ten-thousand/ten_thousand')
    from game_logic import GameLogic

current_round = 0
total_score = 0
unbanked_score = 0
dice = 6
dice_rolled = str()
roll_score = 0
game_status = True
dice_saved = []
round_status = True
hot_dice = False


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
        global hot_dice
        print(f'Rolling {dice} dice...')

        # roll the dice
        dice_rolled = GameLogic.roll_dice(dice)

        # test dice input
        # dice_rolled = (2, 3, 1, 3, 1, 2)

        # Format the string later
        dice_rolled_string = str(dice_rolled[0])
        if len(dice_rolled) >= 2:
            for di in range(1, len(dice_rolled)):
                dice_rolled_string += ', ' + str(dice_rolled[di])

        # Zilch out all 6 dice
        roll_score = GameLogic.calculate_score(dice_rolled)
        hot_dice = GameLogic.check_hot_dice(dice_rolled)


        # roll_score = 0
        if roll_score == 0:
            print(f'*** {dice_rolled_string} ***')
            print('****************************************')
            print('**        Zilch!!! Round over         **')
            print('****************************************')
            print(f"You banked 0 points in round {current_round}")
            print(f"Total score is {total_score}.")
            round_status = False
            return

        # Dice to Keep
        valid_data = False

        while valid_data is False:
            print(f'*** {dice_rolled_string} ***')
            print('Enter dice to keep, or (q)uit:')
            user_input = input('> ')
            if user_input == 'q':
                print(f'Thanks for playing. You earned {total_score} points.')
                game_status = False
                round_status = False
                return
            # else dice to keep, adjust dice to roll and update unbanked points, roll then prompt

            # Check for valid data
            user_input = string_to_list(user_input)
            user_dice_count = count_dice(user_input) # convert to dict
            rolled_dice_count = count_dice(dice_rolled) # convert to dict

            valid_data = True

            print(type(user_input)) # list of dice user wants to keep
            print(type(dice_rolled)) # tuple of full roll

            for di_value in range(1, 7):
                if user_dice_count[di_value] > rolled_dice_count[di_value] or len(user_input) == 0:
                    valid_data = False

            if valid_data is False:
                print('Cheater!!! Or possibly made a typo...')


        dice_saved = dice_saved + user_input
        dice -= len(user_input)

        # Zilch out after dice are kept
        roll_score = GameLogic.calculate_score(user_input)
        hot_dice = GameLogic.check_hot_dice(user_input)

        if roll_score == 0:
            print('****************************************')
            print('**        Zilch!!! Round over         **')
            print('****************************************')
            round_status = False

        # Check for hot dice (6 scoring dice)
        if hot_dice and len(user_input) == len(dice_rolled):
            dice = 6
            print(f'Hot dice: {hot_dice}')




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



