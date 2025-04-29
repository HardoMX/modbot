import discord
import logging
import yaml


with open("secrets.yaml", "r") as file:
    TOKEN = yaml.safe_load(file)["tokens"]["discord"]


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
        print("================")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

        if message.author == client.user:
            return

        if message.content.startswith("$test"):
            await message.channel.send("good test")


intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)

client.run(TOKEN, log_handler=handler)
