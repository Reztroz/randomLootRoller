from dyce import R, H
from dyce.r import ValueRoller

d10 = H(10) - 1     # works with d00 to simulate a roll of a d100 numbers 0-90 (in 10s)
d00 = 10 * d10      # works with d10 to simulate a roll of a d100 number 0-9
d12 = H(12)         # creates histogram for a d12
d8 = H(8)           # creates histogram for a d8
d6 = H(6)           # creates histogram for a d6
d4 = H(4)           # creates histogram for a d4

# creates roll pool for d100 based off of pools for d10 and d00, rolls the 2 roll pools, and then adds them together
r_d100 = R.from_values(d00, d10) ; r_d100
roll1d100 = r_d100.roll()
roll1d100Total = roll1d100.total()

rolld6 = d6.roll()                                   # rolls once on the d6 pool

# works the same as r_d100 above but rolls 2 d6s and adds them together
r_2d6 = ValueRoller(d6) + ValueRoller(d6) ; r_2d6
roll2d6 = r_2d6.roll()
roll2d6Total = roll2d6.total()

# works the same as r_2d6 above but rolls 3 d6s and adds them together
r_3d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_3d6
roll3d6 = r_3d6.roll()
roll3d6Total = roll3d6.total()

# works the same as r_3d6 above but rolls 4 d6s and adds them together
r_4d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_4d6
roll4d6 = r_4d6.roll()
roll4d6Total = roll4d6.total()

# works the same as r_4d6 above but rolls 5 d6s and adds them together
r_5d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6)+ ValueRoller(d6) ; r_5d6
roll5d6 = r_5d6.roll()
roll5d6Total = roll5d6.total()

# works the same as r_5d6 above but rolls 6 d6s and adds them together
r_6d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6)+ ValueRoller(d6) ; r_6d6
roll6d6 = r_6d6.roll()
roll6d6Total = roll6d6.total()

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
        treasure = 'you find ' + str(roll5d6Total) + 'CP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(roll4d6Total) + 'SP'
    elif 60 < roll < 70:
        treasure = 'you find ' + str(roll3d6Total) + 'EP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(roll3d6Total) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(rolld6) + 'PP'

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
        treasure = 'you find ' + str(roll4d6Total * 100) + 'CP and ' + str(rolld6 * 10) + 'EP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(roll6d6Total * 10) + 'SP and ' + str(roll2d6Total * 10) + 'GP'
    elif 60 < roll < 70:
        treasure = 'you find ' + str(roll3d6Total * 10) + 'EP and ' + str(roll2d6Total * 10) + 'GP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(roll4d6Total * 10) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(roll2d6Total * 10) + 'GP and ' + str(roll3d6Total) + 'PP'

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
    if roll < 31:
        treasure = 'you find ' + str(roll5d6Total) + 'CP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(roll4d6Total) + 'SP'
    elif 60 < roll < 70:
        treasure = 'you find ' + str(roll3d6Total) + 'EP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(roll3d6Total) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(rolld6) + 'PP'

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
    if roll < 31:
        treasure = 'you find ' + str(roll5d6Total) + 'CP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(roll4d6Total) + 'SP'
    elif 60 < roll < 70:
        treasure = 'you find ' + str(roll3d6Total) + 'EP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(roll3d6Total) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(rolld6) + 'PP'

    return treasure

print('Enter the CR for the encounter: ')
cr = int(input())

if cr < 5:
    print (cr_4_treasure(roll1d100Total))
elif 4 < cr < 11:
    print(cr_5_treasure(roll1d100Total))
elif 10 < cr < 17:
    print(cr_11_treasure(roll1d100Total))
elif cr > 16:
    print(cr_17_treasure(roll1d100Total))
