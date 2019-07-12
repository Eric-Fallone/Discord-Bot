import random

# DND and dice roll commands


cursor = ""


def chat_hooks(message, cursor_in):
    global cursor
    cursor = cursor_in
    if message.startswith('!20'):
        return roll20()

    if message.startswith('!getStat'):
        return get_ststs(message)

    if message.startswith('!rollStats'):
        return roll_stats()

    if message.startswith('!roll'):
        return roll(message)

    if message.startswith('!ini'):
        return initiative()

    return ""

# rolls a d20 short hand for most used die
# INPUTS: NONE
# OUTPUTS: Random number between 1 and 20


def roll20():
    dice = random.randint(1, 20)
    msg = ('You rolled a: ' + str(dice))
    return msg


# Get Charater Stats
# INPUT: character name, stat to get
# OUTPUT: character stats from database


def get_ststs(message):
    tokens = message.split(' ')
    print(tokens)
    del tokens[0]
    char_name = str(tokens[0])

    getStat = tokens[1]

    msg = 'Getting ' + getStat + " for " + char_name + "\n"

    cursor.execute("""SELECT """ + getStat + """ FROM dndchars.charaters where IsActive = 1 AND NameChar= '""" + char_name + """'""")
    for row in cursor.fetchall():
        msg += str(row[0]) + "\n"

    return msg


# generates a stat block that rolls 4d6 and removes the lowest number
# INPUT: NONE
# OUTPUT: returns stat block and a history showing rolls


def roll_stats():
    roll1 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    roll2 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    roll3 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    roll4 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    roll5 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    roll6 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    removed_rolls = [min(roll1), min(roll2), min(roll3), min(roll4), min(roll5), min(roll6)]

    roll1.remove(min(roll1))
    roll2.remove(min(roll2))
    roll3.remove(min(roll3))
    roll4.remove(min(roll4))
    roll5.remove(min(roll5))
    roll6.remove(min(roll6))

    msg = 'Your stats are:\n\n'

    msg += "First Stat: " + str(sum(roll1)) + " Rolls: " + str(roll1) + " Lowest: " + str(removed_rolls[0]) + "\n"
    msg += "Second Stat: " + str(sum(roll2)) + " Rolls: " + str(roll2) + " Lowest: " + str(removed_rolls[1]) + "\n"
    msg += "Third Stat: " + str(sum(roll3)) + " Rolls: " + str(roll3) + " Lowest: " + str(removed_rolls[2]) + "\n"
    msg += "Fourth Stat: " + str(sum(roll4)) + " Rolls: " + str(roll4) + " Lowest: " + str(removed_rolls[3]) + "\n"
    msg += "Fifth Stat: " + str(sum(roll5)) + " Rolls: " + str(roll5) + " Lowest: " + str(removed_rolls[4]) + "\n"
    msg += "Sixth Stat: " + str(sum(roll6)) + " Rolls: " + str(roll6) + " Lowest: " + str(removed_rolls[5]) + "\n\n"
    msg += "Final Stats are:" + str([sum(roll1), sum(roll2), sum(roll3), sum(roll4), sum(roll5), sum(roll6)])

    return msg


# A dice roll funtion that rolls
# INPUT: Number of dice, Sides of dice in standard dice format ie: 2d6 is rolling 2 six sided dice
# OUTPUT: Dice rolled or error message with wrong format


def roll(message):
    tokens = message.split(' ')
    del tokens[0]
    print(tokens)
    msg = ""
    total = 0
    for token in tokens:
        helper = token.split('d')
        print(helper)
        num_of_rolls = int(helper[0])
        dice_max = int(helper[1])
        x = 0
        msg = msg + "( "
        #dice rolls
        token_rolls = []
        while x < num_of_rolls:
            token_rolls.append(random.randint(1, dice_max))
            msg += (str(token_rolls[x])+" ")
            x += 1
        #modifiers

        #totals / ending rolls
        total += sum(token_rolls)
        msg = msg + ")"

    out_msg = "Total: "+str(total)+"\nRolls: "+msg

    return out_msg;


# Rolls intiative based on the active members in session
# INPUT: None
# OUTPUT: Initive list in order of highest to lowest


def initiative():
    msg = 'Initiative' + "\n"
    # name ,
    data = []
    cursor.execute("SELECT NameChar,Initiative,InitiativeAdv FROM dndchars.charaters where IsActive = 1")
    for row in cursor.fetchall():
        if row[2] is 0:
            roll1 = int(row[1]) + random.randint(1, 20)
            data.append([str(row[0]), roll1])
        else:
            roll1 = int(row[1]) + random.randint(1, 20)
            roll2 = int(row[1]) + random.randint(1, 20)
            data.append([str(row[0]), max(roll1, roll2)])
    data.sort(key=lambda y: -y[1])
    print(data)

    for row in data:
        msg += str(row[0]) + ": " + str(row[1]) + "\n"

    return msg

