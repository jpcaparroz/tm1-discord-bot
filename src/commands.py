import os

from discord import Intents
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN: str = os.getenv('BOT_TOKEN')


intents = Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix='/')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def hello(bot):
    await bot.send("Oi, beleza?")


client.run(TOKEN)