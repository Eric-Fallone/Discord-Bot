# Work with Python 3.6
import discord
import mysql.connector
import config
#chat hooks
import silly
import dnd
from Bot_Commands import BotCommands

TOKEN = config.TOKEN

client = discord.Client()

server = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database,
)

cursor = server.cursor()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    bot_commands = BotCommands(message)
    #await bot_commands.send_message("test")

    inputs = message.content.split(' ')
    root = inputs[0]
    del inputs[0]

    await silly.chat_hooks(bot_commands, root, inputs)  # silly chat hooks can trigger without using a hook
    await dnd.chat_hooks(bot_commands, cursor, root, inputs)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

