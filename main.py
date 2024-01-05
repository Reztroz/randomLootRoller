from dyce import R, H
from dyce.r import ValueRoller

def diceRoller(numdice, sizedice):

    d10 = H(10) - 1     # works with d00 to simulate a roll of a d100 numbers 0-90 (in 10s)
    d00 = 10 * d10      # works with d10 to simulate a roll of a d100 number 0-9
    d12 = H(12)         # creates histogram for a d12
    d8 = H(8)           # creates histogram for a d8
    d6 = H(6)           # creates histogram for a d6
    d4 = H(4)           # creates histogram for a d4

    total = 0

    # creates roll pools for dice
    r_d100 = R.from_values(d00, d10) ; r_d100

    r_2d6 = ValueRoller(d6) + ValueRoller(d6) ; r_2d6

    r_3d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_3d6

    r_4d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_4d6

    r_5d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_5d6

    r_6d6 = ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) ; r_6d6

    r_8d6 = (ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) + ValueRoller(d6) +
         ValueRoller(d6) + ValueRoller(d6)) ; r_8d6

    if numdice == 1 and sizedice == 100:
        total = r_d100.roll().total()
    elif numdice == 1 and sizedice == 6:
        total = d6.roll()
    elif numdice == 2 and sizedice == 6:
        total = r_2d6.roll().total()
    elif  numdice == 3 and sizedice == 6:
        total = r_3d6.roll().total()
    elif  numdice == 4 and sizedice == 6:
        total = r_4d6.roll().total()
    elif  numdice == 5 and sizedice == 6:
        total = r_5d6.roll().total()
    elif  numdice == 6 and sizedice == 6:
        total = r_6d6.roll().total()
    elif  numdice == 8 and sizedice == 6:
        total = r_8d6.roll().total()

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
        treasure = 'you find ' + str(diceRoller(5, 6)) + 'CP'
    elif 30 < roll < 61:
        treasure = 'you find ' + str(diceRoller(4, 6)) + 'SP'
    elif 60 < roll < 71:
        treasure = 'you find ' + str(diceRoller(3, 6)) + 'EP'
    elif 70 < roll < 96:
        treasure = 'you find ' + str(diceRoller(3, 6)) + 'GP'
    elif roll > 95:
        treasure = 'you find ' + str(diceRoller(1, 6)) + 'PP'

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
        treasure = ('you find ' + str(diceRoller(4, 6) * 100) + 'CP and ' +
                    str(diceRoller(1, 6) * 10) + 'EP')
    elif 30 < roll < 61:
        treasure = ('you find ' + str(diceRoller(6, 6) * 10) + 'SP and ' +
                    str(diceRoller(2, 6) * 10) + 'GP')
    elif 60 < roll < 71:
        treasure = ('you find ' + str(diceRoller(3, 6) * 10) + 'EP and ' +
                    str(diceRoller(2, 6) * 10) + 'GP')
    elif 70 < roll < 96:
        treasure = 'you find ' + str(diceRoller(4, 6) * 10) + 'GP'
    elif roll > 95:
        treasure = ('you find ' + str(diceRoller(2, 6) * 10) + 'GP and ' +
                    str(diceRoller(3, 6)) + 'PP')

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
        treasure = ('you find ' + str(diceRoller(4, 6) * 100) + 'SP and ' +
                    str(diceRoller(1, 6) * 100) + 'GP')
    elif 20 < roll < 36:
        treasure = ('you find ' + str(diceRoller(1, 6) * 100) + 'EP and ' +
                    str(diceRoller(1, 6) * 100) + 'GP')
    elif 35 < roll < 76:
        treasure = ('you find ' + str(diceRoller(2, 6) * 100) + 'GP and ' +
                    str(diceRoller(1, 6) * 10) + 'PP')
    elif roll > 75:
        treasure = ('you find ' + str(diceRoller(2, 6) * 100) + 'GP and' +
                    str(diceRoller(2, 6) * 10) + 'PP')

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
        treasure = ('you find ' + str(diceRoller(2, 6) * 1000) + 'EP and ' +
                    str(diceRoller(8, 6) * 100) + 'GP')
    elif 15 < roll < 56:
        treasure = ('you find ' + str(diceRoller(1, 6) * 1000) + 'GP and ' +
                    str(diceRoller(1, 6) * 100) + 'PP')
    elif roll > 55:
        treasure = ('you find ' + str(diceRoller(1, 6) * 1000) + 'GP and ' +
                    str(diceRoller(2, 6) * 100) + 'PP')

    return treasure

print('Enter the CR for the encounter: ')
cr = int(input())

roll = diceRoller(1, 100)

if cr < 5:
    print (cr_4_treasure(roll))
elif 4 < cr < 11:
    print(cr_5_treasure(roll))
elif 10 < cr < 17:
    print(cr_11_treasure(roll))
elif cr > 16:
    print(cr_17_treasure(roll))