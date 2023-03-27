from collections import Counter
import random

class GameLogic:
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

        score = 0

        # Handle the case where the dice list is empty.
        if not dice_list:
            return score

        # Check for a straight.
        if set(dice_list) == {1, 2, 3, 4, 5, 6}:
            return 1500

        # Check for three pairs.
        value_counts = Counter(dice_list)
        if len(value_counts) == 3 and all(count == 2 for count in value_counts.values()):
            score += 1500
            # for value in value_counts.keys():
            #     if value != 1 and value != 5:
            #         score += value * 100

        # Check for three-of-a-kind or higher.
        for value in set(dice_list):
            count = dice_list.count(value)
            base_score = 0

            if count >= 3:
                if value == 1:
                    base_score = 1000
                else:
                    base_score = 100 * value

                if count == 4:
                    base_score = base_score * 2

                elif count == 5:
                    base_score = base_score * 3

                elif count == 6:
                    base_score = base_score * 4

                score += base_score

                for i in range(count):
                    dice_list.remove(value)

        # Add any remaining 1s or 5s.
        for value in dice_list:
            if value == 1:
                score += 100
            elif value == 5:
                score += 50

        return score

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

if __name__ == '__main__':
    game = GameLogic()
    my_dice = [3,3,3,3,3,4]
    print(game.calculate_score(my_dice))

