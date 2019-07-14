import random

# DND and dice roll commands


async def chat_hooks(bot_commands, cursor, root, inputs):

    if root == '!20':
        await roll20(bot_commands)

    if root == '!getStat':
        await get_ststs(bot_commands, cursor, inputs)

    if root == '!rollStats':
        await roll_stats(bot_commands, inputs)

    if root == '!roll':
        await roll(bot_commands, inputs)

    if root == '!ini':
        await initiative(bot_commands, cursor)

    return

# rolls a d20 short hand for most used die
# INPUTS: NONE
# OUTPUTS: Random number between 1 and 20


async def roll20(bot_commands):
    dice = random.randint(1, 20)
    out_msg = ('You rolled a: ' + str(dice))
    await bot_commands.send_message(out_msg)


# Get Character Stats
# INPUT: character name, stat to get
# OUTPUT: character stats from database


async def get_ststs(bot_commands, cursor, inputs):
    char_name = str(inputs[0])

    getStat = inputs[1]

    msg = 'Getting ' + getStat + " for " + char_name + "\n"

    cursor.execute("""SELECT """ + getStat + """ FROM dndchars.charaters where IsActive = 1 AND NameChar= '""" + char_name + """'""")
    for row in cursor.fetchall():
        msg += str(row[0]) + "\n"

        await bot_commands.send_message(msg)


# generates a stat block that rolls 4d6 and removes the lowest number
# INPUT: NONE
# OUTPUT: returns stat block and a history showing rolls


async def roll_stats(bot_commands):
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

    await bot_commands.send_message(msg)


# A dice roll funtion that rolls
# INPUT: Number of dice, Sides of dice in standard dice format ie: 2d6 is rolling 2 six sided dice
# OUTPUT: Dice rolled or error message with wrong format


async def roll(bot_commands, inputs):
    msg = ""
    total = 0
    for token in inputs:
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

    msg = "Total: "+str(total)+"\nRolls: "+msg

    await bot_commands.send_message(msg)


# Rolls intiative based on the active members in session
# INPUT: None
# OUTPUT: Initive list in order of highest to lowest


async def initiative(bot_commands, cursor):
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

    await bot_commands.send_message(msg)

