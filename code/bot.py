import discord
import config


class MyBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if (message.content == "seal"):
            print('Message from {0.author}: {0.content}'.format(message))
            await
            message.channel.send("otter")

        if (message.content == "whoami"):
            print('Message from {0.author}: {0.content}'.format(message))
            await
            message.channel.send('You are {0.author}'.format(message))
            # breakpoint()
            await
            message.channel.send("test")
            message.channel.send("otter")

        if (message.content == "emote"):
            print('Message from {0.author}: {0.content}'.format(message))
            await
            # message.channel.send('You are {0.author}'.format(message))
            # breakpoint()
            await
            message.channel.send("<a:petJules:769223894749151292>")
            
        if (message.content == "Voice"):
            print('Message from {0.author}: {0.content}'.format(message))
            channel = discord.utils.get(message.guild.channels, name="music")
            voicechannel = await
            channel.connect()
            # voicechannel.play(discord.PCMAudio('test.wav'))
            # breakpoint()
            voicechannel.play(discord.FFmpegPCMAudio('test.mp3'))


client = MyBot()
client.run(config.discordSecret)
