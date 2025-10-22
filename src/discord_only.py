from dotenv import load_dotenv
import discord
import os

# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True # Ensure that your bot can read message content

client = discord.Client(intents=intents)

# Define an event handler for when the bot is ready.
@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
