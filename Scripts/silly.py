#silly functions module


def chat_hooks(message):
    if 'http://getcomfy.in/l_egu' in message:
        out_msg = "No one wants to buy your underwear Love"
        return out_msg

    if message.startswith('!hello'):
        return 'Hello {0.author.mention}'.format(message)

    return "", ""