#
#  Bot commands where the discord server is actually affective
#


class BotCommands:
    def __init__(self, message):
        self.message = message

    async def send_message(self, msg):
        await self.message.channel.send(msg)

    async def delete_message(self, msg):
        await self.message.channel.send(msg)
