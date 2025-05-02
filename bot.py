# Azure
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Discord
import discord
from discord.ext import commands

import logging

logger = logging.getLogger(__name__)

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url = "https://modbot.vault.azure.net/",
    credential = credential
)

TOKEN = client.get_secret("discord-token").value


intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(name="You", type=discord.ActivityType.watching)

bot = commands.Bot(command_prefix="$", intents=intents, activity=activity)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    logger.info(f"Logged in as {bot.user}!")
    print("================")
    logger.info("================")

@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")
    logger.info(f"Message from {message.author}: {message.content}")

    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("good test")


async def run_bot():
    logger.info("Bot starting")
    await bot.start(TOKEN)
