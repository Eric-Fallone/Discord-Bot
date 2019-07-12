# Work with Python 3.6
import discord
import mysql.connector
import config
#chat hooks
import silly
import dnd

TOKEN = config.TOKEN

client = discord.Client()

serv = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database,
)

cursor = serv.cursor()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    msg = silly.chat_hooks(message.content)
    msg = dnd.chat_hooks(message.content, cursor)
    if msg is not "":
        await message.channel.send(msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)