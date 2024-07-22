import os

from discord import Client
from discord import Intents

from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN: str = os.getenv('BOT_TOKEN')


intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('o filipe é gay?'):
        await message.channel.send('Acho que sim...')


client.run(TOKEN)