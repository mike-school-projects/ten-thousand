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
        score = 0

        # Handle the case where the dice list is empty.
        if not dice:
            return score

        # Check for a straight.
        if set(dice) == {1, 2, 3, 4, 5, 6}:
            return 1500

        # Check for three pairs.
        value_counts = Counter(dice)
        if len(value_counts) == 3 and all(count == 2 for count in value_counts.values()):
            score += 1000
            for value in value_counts.keys():
                if value != 1 and value != 5:
                    score += value * 100

        # Check for three-of-a-kind or higher.
        for value in set(dice):
            count = dice.count(value)
            if count >= 3:
                if value == 1:
                    score += 1000 if count == 3 else 1000 + (count - 3) * 100
                elif value == 5:
                    score += 500 if count == 3 else 500 + (count - 3) * 50
                else:
                    score += value * 100 * (2 ** (count - 3))
                for i in range(3):
                    dice.remove(value)

        # Add any remaining 1s or 5s.
        for value in dice:
            if value == 1:
                score += 100
            elif value == 5:
                score += 50

        # Check if there is a chance to complete a straight.
        if len(set(dice)) >= 5:
            remaining_values = set(range(1, 7)) - set(dice)
            if len(remaining_values) == 1:
                value = remaining_values.pop()
                if value == 1:
                    score += 100
                elif value == 5:
                    score += 50
                else:
                    score = 0
            elif len(remaining_values) == 2:
                score += 500

        return score
