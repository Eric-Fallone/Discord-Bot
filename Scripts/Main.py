# Work with Python 3.6
import discord
import random
import tokenize
import mysql.connector
import config


TOKEN = config.TOKEN

client = discord.Client()

serv = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database,
    auth_plugin='mysql_native_password'
)

cursor = serv.cursor()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!20'):
        roll = random.randint(1,20)
        msg = ('You rolled a: '+str(roll)).format(message)
        await client.send_message(message.channel, msg)


    if message.content.startswith('!getStat'):
        tokens = message.content.split(' ')
        print(tokens)
        del tokens[0]
        charName= str(tokens[0])

        getStat=tokens[1]

        msg = 'Getting '+getStat+" for "+charName+ "\n"

        cursor.execute("""SELECT """ +getStat+""" FROM dndchars.charaters where IsActive = 1 AND NameChar= '"""+charName+"""'""")
        for row in cursor.fetchall():
            msg += str(row[0]) + "\n"

        await client.send_message(message.channel, msg)



    if message.content.startswith('!stats'):
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
        msg += "Final Stats are:"+str([sum(roll1), sum(roll2), sum(roll3), sum(roll4), sum(roll5), sum(roll6)])

        await client.send_message(message.channel, msg)

    if message.content.startswith('!roll'):
        tokens = message.content.split(' ')
        del tokens[0]
        #for each token ie 1d6+10
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


        await client.send_message(message.channel, out_msg)



    if message.content.startswith('!ini'):
        msg = 'Initiative' + "\n"
        # name ,
        data = []
        cursor.execute("SELECT NameChar,Initiative,InitiativeAdv FROM dndchars.charaters where IsActive = 1")
        for row in cursor.fetchall():
            if row[2] is 0:
                roll1 = int(row[1]) + random.randint(1, 20)
                data.append([str(row[0]),roll1])
            else:
                roll1 = int(row[1]) + random.randint(1, 20)
                roll2 = int(row[1]) + random.randint(1, 20)
                data.append([str(row[0]), max(roll1, roll2)])
        data.sort(key=lambda y: -y[1])
        print(data)

        for row in data:
            msg += str(row[0]) +": "+ str(row[1]) + "\n"

        await client.send_message(message.channel, msg)

    if 'http://getcomfy.in/l_egu' in message.content:
        tempMsgChan = message.channel
        await client.delete_message(message)
        out_msg = "No one wants to buy your underwear Love"
        await client.send_message(tempMsgChan, out_msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)