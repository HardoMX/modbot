import asyncio
import logging

# Azure
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Discord
import discord
from discord.ext import commands

# API
import uvicorn
from fastapi import FastAPI


credential = DefaultAzureCredential()

client = SecretClient(
    vault_url = "https://modbot.vault.azure.net/",
    credential = credential
)

TOKEN = client.get_secret("discord-token").value


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")


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


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "API Active"}


async def run_api():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def run_bot():
    await bot.start(TOKEN)

async def main():
    await asyncio.gather(run_bot(), run_api())


if __name__ == "__main__":
    asyncio.run(main())
