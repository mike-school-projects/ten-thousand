from collections import Counter
import random

class GameLogic:
    # Bulk of this code from ChatGPT
    @staticmethod
    def calculate_score(dice):
        """
        Calculate the score based on the given list of dice.

        Args:
            dice (list[int]): A list of integers representing the values of the dice.

        Returns:
            int: The total score for the given dice.
        """

        # change input to list
        dice_list = list(dice)

        # initialize variables
        hot_dice = False
        ones_and_fives_needed_for_hot_dice = len(dice)
        score = 0
        count_1_5 = 0
        scoring_dice = list()

        # Handle the case where the dice list is empty.
        if not dice_list:
            return score

        # Check for a straight.
        if set(dice_list) == {1, 2, 3, 4, 5, 6}:
            hot_dice = True
            scoring_dice = dice_list
            return 1500

        # Check for three pairs.  Counts how many of each result there is.
        # 3 pairs occurs if the count is 2 (i.e. pairs), and the length is 3 (i.e. 3 pairs)
        value_counts = Counter(dice_list)
        if len(value_counts) == 3 and all(count == 2 for count in value_counts.values()):
            # score += 1500
            hot_dice = True
            scoring_dice = dice_list
            return 1500

        # Check for three-of-a-kind or higher.
        # iterate through dice_list for each value.  Count how many there are.
        for value in set(dice_list):
            count = dice_list.count(value)
            base_score = 0

            # Check for 3 of a kind or greater
            if count >= 3:
                scoring_dice.append(value)
                scoring_dice.append(value)
                scoring_dice.append(value)

                # Calculate base_score for 3 of a kind
                if value == 1:
                    base_score = 1000
                    ones_and_fives_needed_for_hot_dice -= 3

                else:
                    base_score = 100 * value

                if value == 5:
                    ones_and_fives_needed_for_hot_dice -= 3

                # Check for 4 of a kind
                if count == 4:
                    base_score = base_score * 2
                    ones_and_fives_needed_for_hot_dice -= 4
                    scoring_dice.append(value)

                # Check for 5 of a kind
                elif count == 5:
                    base_score = base_score * 3
                    ones_and_fives_needed_for_hot_dice -= 5
                    scoring_dice.append(value)
                    scoring_dice.append(value)

                elif count == 6:
                    base_score = base_score * 4
                    hot_dice = True
                    scoring_dice = dice_list

                # Add to total score
                score += base_score

                # After scoring the value, remove it from the list of dice and repeat loop
                for i in range(count):
                    dice_list.remove(value)

        for value in dice_list:
            if value == 1:
                score += 100
                count_1_5 += 1
                scoring_dice.append(value)
            elif value == 5:
                score += 50
                count_1_5 += 1
                scoring_dice.append(value)

        # Compare to number of 1' and 5's needed for hot dice
        if ones_and_fives_needed_for_hot_dice == count_1_5:
            hot_dice = True

        return score

    def check_hot_dice(dice):
        """
        Calculate the score based on the given list of dice.

        Args:
            dice (list[int]): A list of integers representing the values of the dice.

        Returns:
            int: The total score for the given dice.
        """

        # change input to list
        dice_list = list(dice)

        # initialize variables
        hot_dice = False
        ones_and_fives_needed_for_hot_dice = len(dice)
        score = 0
        count_1_5 = 0
        scoring_dice = list()

        # Handle the case where the dice list is empty.
        if not dice_list:
            return hot_dice

        # Check for a straight.
        if set(dice_list) == {1, 2, 3, 4, 5, 6}:
            hot_dice = True
            scoring_dice = dice_list
            return hot_dice

        # Check for three pairs.  Counts how many of each result there is.
        # 3 pairs occurs if the count is 2 (i.e. pairs), and the length is 3 (i.e. 3 pairs)
        value_counts = Counter(dice_list)
        if len(value_counts) == 3 and all(count == 2 for count in value_counts.values()):
            # score += 1500
            hot_dice = True
            scoring_dice = dice_list
            return hot_dice

        # Check for three-of-a-kind or higher.
        # iterate through dice_list for each value.  Count how many there are.
        for value in set(dice_list):
            count = dice_list.count(value)
            base_score = 0

            # Check for 3 of a kind or greater
            if count >= 3:
                scoring_dice.append(value)
                scoring_dice.append(value)
                scoring_dice.append(value)

                # Calculate base_score for 3 of a kind
                if value == 1:
                    base_score = 1000
                    ones_and_fives_needed_for_hot_dice -= 3

                else:
                    base_score = 100 * value

                if value == 5:
                    ones_and_fives_needed_for_hot_dice -= 3

                # Check for 4 of a kind
                if count == 4:
                    base_score = base_score * 2
                    ones_and_fives_needed_for_hot_dice -= 4
                    scoring_dice.append(value)

                # Check for 5 of a kind
                elif count == 5:
                    base_score = base_score * 3
                    ones_and_fives_needed_for_hot_dice -= 5
                    scoring_dice.append(value)
                    scoring_dice.append(value)

                elif count == 6:
                    base_score = base_score * 4
                    hot_dice = True
                    scoring_dice = dice_list

                # Add to total score
                score += base_score

                # After scoring the value, remove it from the list of dice and repeat loop
                for i in range(count):
                    dice_list.remove(value)

        for value in dice_list:
            if value == 1:
                score += 100
                count_1_5 += 1
                scoring_dice.append(value)
            elif value == 5:
                score += 50
                count_1_5 += 1
                scoring_dice.append(value)

        # Compare to number of 1' and 5's needed for hot dice
        if ones_and_fives_needed_for_hot_dice == count_1_5:
            hot_dice = True

        return hot_dice

    def calculate_scoring_dice(dice):
        """
        Calculate the score based on the given list of dice.

        Args:
            dice (list[int]): A list of integers representing the values of the dice.

        Returns:
            int: The total score for the given dice.
        """

        # change input to list
        dice_list = list(dice)

        # initialize variables
        hot_dice = False
        ones_and_fives_needed_for_hot_dice = len(dice)
        score = 0
        count_1_5 = 0
        scoring_dice = list()

        # Handle the case where the dice list is empty.
        if not dice_list:
            return tuple(scoring_dice)

        # Check for a straight.
        if set(dice_list) == {1, 2, 3, 4, 5, 6}:
            hot_dice = True
            scoring_dice = dice_list
            return tuple(scoring_dice)

        # Check for three pairs.  Counts how many of each result there is.
        # 3 pairs occurs if the count is 2 (i.e. pairs), and the length is 3 (i.e. 3 pairs)
        value_counts = Counter(dice_list)
        if len(value_counts) == 3 and all(count == 2 for count in value_counts.values()):
            # score += 1500
            hot_dice = True
            scoring_dice = dice_list
            return tuple(scoring_dice)

        # Check for three-of-a-kind or higher.
        # iterate through dice_list for each value.  Count how many there are.
        for value in set(dice_list):
            count = dice_list.count(value)
            base_score = 0

            # Check for 3 of a kind or greater
            if count >= 3:
                scoring_dice.append(value)
                scoring_dice.append(value)
                scoring_dice.append(value)

                # Calculate base_score for 3 of a kind
                if value == 1:
                    base_score = 1000
                    ones_and_fives_needed_for_hot_dice -= 3

                else:
                    base_score = 100 * value

                if value == 5:
                    ones_and_fives_needed_for_hot_dice -= 3

                # Check for 4 of a kind
                if count == 4:
                    base_score = base_score * 2
                    ones_and_fives_needed_for_hot_dice -= 4
                    scoring_dice.append(value)

                # Check for 5 of a kind
                elif count == 5:
                    base_score = base_score * 3
                    ones_and_fives_needed_for_hot_dice -= 5
                    scoring_dice.append(value)
                    scoring_dice.append(value)

                elif count == 6:
                    base_score = base_score * 4
                    hot_dice = True
                    scoring_dice = dice_list

                # Add to total score
                score += base_score

                # After scoring the value, remove it from the list of dice and repeat loop
                for i in range(count):
                    dice_list.remove(value)

        for value in dice_list:
            if value == 1:
                score += 100
                count_1_5 += 1
                scoring_dice.append(value)
            elif value == 5:
                score += 50
                count_1_5 += 1
                scoring_dice.append(value)

        # Compare to number of 1' and 5's needed for hot dice
        if ones_and_fives_needed_for_hot_dice == count_1_5:
            hot_dice = True

        return tuple(scoring_dice)


    @staticmethod
    def roll_dice(num_dice):
        """
        Roll the specified number of dice and return the result as a tuple.

        Args:
            num_dice (int): The number of dice to roll.

        Returns:
            tuple[int]: The values of the rolled dice.
        """
        dice = [random.randint(1, 6) for _ in range(num_dice)]
        return tuple(dice)

    @staticmethod
    def get_scorers(input_dice):
        # input in tuple of dice
        # output tuple of dice that are scoring dice
        scorers = GameLogic.calculate_scoring_dice(input_dice)
        return scorers

    @staticmethod
    def validate_keepers(roll, keepers):
        valid_data = True

        roll_dict = GameLogic.count_dice(roll)
        keepers_dict = GameLogic.count_dice(keepers)

        for di_value in range(1, 7):
            if keepers_dict[di_value] > roll_dict[di_value] or len(roll) == 0:
                valid_data = False

        # if valid_data is False:
        #     print('Cheater!!! Or possibly made a typo...')

        return valid_data

    @staticmethod
    def count_dice(dice_to_count):
        # input is going to be a list of dice
        # output is a dict of counts for each result
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

if __name__ == '__main__':
    game = GameLogic()
    my_dice = [3,2,3,1,1,2]

    scorers = game.get_scorers(my_dice)

    print(scorers)
