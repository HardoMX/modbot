# Azure
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Discord
import discord
from discord.ext import commands


credential = DefaultAzureCredential()

client = SecretClient(
    vault_url = "https://modbot.vault.azure.net/",
    credential = credential
)

TOKEN = client.get_secret("discord-token").value


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")
    print("================")

@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")

    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("good test")


async def run_bot():
    await bot.start(TOKEN)
