import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

        if message.author == client.user:
            return

        if message.content.startswith("$test"):
            await message.channel.send("good test")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run("<token>")
