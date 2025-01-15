import random

def rolling_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_sum = dice1 + dice2
    dice_product = dice1 * dice2

    print(f"Your first dice is {dice1}, your second dice is {dice2}. The sum of your dice is {dice_sum}, but your product is {dice_product}")
