"""
Module: randomLootRoller

This module provides functions to simulate dice rolls for generating loot based on challenge ratings (CR) in DND 5e.

Functions:
- `dice_roller(num_dice, size_dice)`: Simulates the rolling of dice with specified parameters and returns the total.
- `cr_4_treasure(roll)`: Calculate loot for CR 4 encounters based on the given roll value.
- `cr_5_treasure(roll)`: Calculate loot for CR 5 encounters based on the given roll value.
- `cr_11_treasure(roll)`: Calculate loot for CR 11 encounters based on the given roll value.
- `cr_17_treasure(roll)`: Calculate loot for CR 17 encounters based on the given roll value.

Usage:
1. Import the module: `from randomLootRoller import *`
2. Enter the CR for the encounter: `cr = int(input())`
3. Generate a random roll: `roll = dice_roller(1, 100)`
4. Calculate and print the treasure based on CR: `print(cr_4_treasure(roll))`, `print(cr_5_treasure(roll))`, etc.

Note: The module uses the Dyce library for dice rolling. Ensure the library is installed before using this module.

Examples:
- Simulating treasure for a CR 5 encounter: `cr_5_treasure(roll)`
"""

from dyce import R, H
from dyce.r import ValueRoller


def dice_roller(num_dice, size_dice):
    """
    Simulates the rolling of dice with specified parameters and returns the total.

    Args:
        num_dice (int): The number of dice to roll.
        size_dice (int): The number of sides on each die.

    Returns:
        int: The total result of the dice rolls.

    Raises:
        ValueError: If the combination of num_dice and size_dice is not supported.
    """

    #  Define histogram for various dice
    d10 = H(10) - 1     # works with d00 to simulate a roll of a d100 numbers 0-9
    d00 = 10 * d10      # works with d10 to simulate a roll of a d100 number 0-90 (in 10s
    d12 = H(12)         # creates histogram for a d12
    d8 = H(8)           # creates histogram for a d8
    d6 = H(6)           # creates histogram for a d6
    d4 = H(4)           # creates histogram for a d4

    total = 0

    # Create roll pools for dice
    r_d100 = R.from_values(d00, d10) ; r_d100

    r_d4 = R.from_value(d4) ; r_d4

    r_d6 = R.from_value(d6) ; r_d6

    r_2d6 = 2@r_d6 ; r_2d6

    r_3d6 = 3@r_d6 ; r_3d6

    r_4d6 = 4@r_d6 ; r_4d6

    r_5d6 = 5@r_d6 ; r_5d6

    r_6d6 = 6@r_d6 ; r_6d6

    r_8d6 = 8@r_d6 ; r_8d6

    r_2d4 = 2@r_d4 ; r_2d4

    # Roll dice based on number of dice sides and qty of dice
    if num_dice == 1 and size_dice == 100:
        total = r_d100.roll().total()
        if total == 0:
            total = total + 100
    elif num_dice == 1 and size_dice == 6:
        total = r_d6.roll().total()
    elif num_dice == 2 and size_dice == 6:
        total = r_2d6.roll().total()
    elif num_dice == 3 and size_dice == 6:
        total = r_3d6.roll().total()
    elif num_dice == 4 and size_dice == 6:
        total = r_4d6.roll().total()
    elif num_dice == 5 and size_dice == 6:
        total = r_5d6.roll().total()
    elif num_dice == 6 and size_dice == 6:
        total = r_6d6.roll().total()
    elif num_dice == 8 and size_dice == 6:
        total = r_8d6.roll().total()
    elif num_dice == 1 and size_dice == 4:
        total = r_d4.roll().total()
    elif num_dice == 2 and size_dice == 4:
        total = r_2d4.roll().total()
    elif num_dice == 1 and size_dice == 8:
        total = d8.roll()
    elif num_dice == 1 and size_dice == 10:
        total = d10.roll()
        if total == 0:
            total = total + 10
    elif num_dice == 1 and size_dice == 12:
        total = d12.roll()
    else:
        raise ValueError("Unsupported combination of num_dice and size_dice.")

    return total


def cr_4_treasure(roll):
    """
    Calculate the treasure based on the given roll value.

    Parameters:
    roll (int): The roll value.

    Returns:
    str: The treasure description.
    """
    treasure = ''
    if roll < 31:
        treasure = 'you find ' + str(dice_roller(5, 6)) + 'CP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(dice_roller(4, 6)) + 'SP'
    elif 60 < roll < 71:
        treasure = 'you find ' + str(dice_roller(3, 6)) + 'EP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(dice_roller(3, 6)) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(dice_roller(1, 6)) + 'PP'

    return treasure


def cr_5_treasure(roll):
    """
    Calculate the treasure based on the given roll value.

    Parameters:
    roll (int): The roll value.

    Returns:
    str: The treasure description.
    """
    treasure = ''
    if roll < 31:
        treasure = ('you find ' + str(dice_roller(4, 6) * 100) + 'CP and ' +
                    str(dice_roller(1, 6) * 10) + 'EP')
    elif 30 < roll < 61:
        treasure = ('you find ' + str(dice_roller(6, 6) * 10) + 'SP and ' +
                    str(dice_roller(2, 6) * 10) + 'GP')
    elif 60 < roll < 71:
        treasure = ('you find ' + str(dice_roller(3, 6) * 10) + 'EP and ' +
                    str(dice_roller(2, 6) * 10) + 'GP')
    elif 70 < roll < 96:
        treasure = 'you find ' + str(dice_roller(4, 6) * 10) + 'GP'
    elif roll > 95:
        treasure = ('you find ' + str(dice_roller(2, 6) * 10) + 'GP and ' +
                    str(dice_roller(3, 6)) + 'PP')

    return treasure


def cr_11_treasure(roll):
    """
    Calculate the treasure based on the given roll value.

    Parameters:
    roll (int): The roll value.

    Returns:
    str: The treasure description.
    """
    treasure = ''
    if roll < 21:
        treasure = ('you find ' + str(dice_roller(4, 6) * 100) + 'SP and ' +
                    str(dice_roller(1, 6) * 100) + 'GP')
    elif 20 < roll < 36:
        treasure = ('you find ' + str(dice_roller(1, 6) * 100) + 'EP and ' +
                    str(dice_roller(1, 6) * 100) + 'GP')
    elif 35 < roll < 76:
        treasure = ('you find ' + str(dice_roller(2, 6) * 100) + 'GP and ' +
                    str(dice_roller(1, 6) * 10) + 'PP')
    elif roll > 75:
        treasure = ('you find ' + str(dice_roller(2, 6) * 100) + 'GP and' +
                    str(dice_roller(2, 6) * 10) + 'PP')

    return treasure


def cr_17_treasure(roll):
    """
    Calculate the treasure based on the given roll value.

    Parameters:
    roll (int): The roll value.

    Returns:
    str: The treasure description.
    """
    treasure = ''
    if roll < 16:
        treasure = ('you find ' + str(dice_roller(2, 6) * 1000) + 'EP and ' +
                    str(dice_roller(8, 6) * 100) + 'GP')
    elif 15 < roll < 56:
        treasure = ('you find ' + str(dice_roller(1, 6) * 1000) + 'GP and ' +
                    str(dice_roller(1, 6) * 100) + 'PP')
    elif roll > 55:
        treasure = ('you find ' + str(dice_roller(1, 6) * 1000) + 'GP and ' +
                    str(dice_roller(2, 6) * 100) + 'PP')

    return treasure


print('Enter the CR for the encounter: ')
cr = int(input())

roll = dice_roller(1, 100)

if cr < 5:
    print(cr_4_treasure(roll))
elif 4 < cr < 11:
    print(cr_5_treasure(roll))
elif 10 < cr < 17:
    print(cr_11_treasure(roll))
elif cr > 16:
    print(cr_17_treasure(roll))
