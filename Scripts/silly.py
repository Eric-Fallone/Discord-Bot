import random
# silly functions module

async def chat_hooks(bot_commands, root, inputs):

    if 'http://getcomfy.in/l_egu' in inputs or root == 'http://getcomfy.in/l_egu':
        await no_one_wants_to_buy_it_kyle(bot_commands)

    if 'uno' in inputs or root == 'uno':
        await uno(bot_commands)

    if root == '!hello':
        print(root is '!hello')
        await bot_commands.send_message("Hello")

    return


async def no_one_wants_to_buy_it_kyle(bot_commands):
    out_msg = "No one wants to buy your underwear Love"
    await bot_commands.send_message(out_msg)


async def uno(bot_commands):

    choice = random.randint(0, 4)

    cards = ["https://cdn.discordapp.com/attachments/161704316867051520/615965939556679694/image0.jpg",
             "https://cdn.discordapp.com/attachments/161704316867051520/615966210592604173/image0.jpg",
             "https://cdn.discordapp.com/attachments/161704316867051520/615981402747305985/image0.jpg",
             "https://s4.scoopwhoop.com/anj/sw/31eb1dc4-b01c-4a9b-823e-cd11be24b5eb.jpg",
             "https://s4.scoopwhoop.com/anj/sw/ba1579b1-f0e9-410c-a912-90fb8ca8d2fc.jpg"]

    out_msg = cards[choice]

    await bot_commands.send_message(out_msg)

async def hello(bot_commands):
    out_msg = "Hello!"
    await bot_commands.send_message(out_msg)
