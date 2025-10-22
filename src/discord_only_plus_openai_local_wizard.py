from dotenv import load_dotenv
from openai import OpenAI, completions #OpenAI library
#testing to see if lmstudio import is even needed with this implementation
#import lmstudio as lms
import discord
import os

# Load environment variables from .env file
load_dotenv()
# set openai api key that was loaded from the .env file 
OPENAI_KEY = os.getenv('OPENAI_KEY')
# original OpenAI client definition
#oa_client = OpenAI(api_key=OPENAI_KEY)
# 
# LM Studio client definition
#changes for using lmstudio locally instead of openai
# Ensure LM Studio server is running on the specified host and port
# SERVER_API_HOST = "localhost:1234"
oa_client = OpenAI(
    base_url="http://localhost:1234/v1",  # Replace 1234 with your LM Studio server port if different
    api_key="lm-studio"  # This API key is required but unused by LM Studio's local server
)

# ask openai - respond like a pirate function
# for test replace model="gpt-4o" with model="gpt-oss-20b"
def call_openai(question):
    # Call the OpenAI API
    completion = oa_client.chat.completions.create(
        model="open-ai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": f"Respond like a wizard to the following question: {question}",
            },
        ]
    )

    #Print the response
    response = completion.choices[0].message.content
    print(response)
    return response

# Set up intents
intents = discord.Intents.default()
intents.message_content = True # Ensure that your bot can read message content
client = discord.Client(intents=intents)

# Define an event handler for when the bot is ready.
@client.event
async def on_ready():
 #   print(f'Logged in as {client.user}!')
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question")[1]
        print(f"Question: {message.content}")
        response = call_openai(message_content)
        print(f"Assistant: {response}")
        print("---")
        await message.channel.send(response)

    if message.content.startswith('$wizard'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$wizard")[1]
        print(f"Question: {message.content}")
        response = call_openai(message_content)
        print(f"Assistant: {response}")
        print("---")
        await message.channel.send(response)

client.run(os.getenv('DISCORD_WIZARD_TOKEN'))
