# silly functions module


async def chat_hooks(bot_commands, root, inputs):

    if 'http://getcomfy.in/l_egu' in inputs or root == 'http://getcomfy.in/l_egu':
        await no_one_wants_to_buy_it_kyle(bot_commands)

    if root == '!hello':
        print(root is '!hello')
        await bot_commands.send_message("Hello")

    return


async def no_one_wants_to_buy_it_kyle(bot_commands):
    out_msg = "No one wants to buy your underwear Love"
    await bot_commands.send_message(out_msg)


async def hello(bot_commands):
    out_msg = "Hello!"
    await bot_commands.send_message(out_msg)
