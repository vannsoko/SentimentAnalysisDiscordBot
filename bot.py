import datetime
import os
import asyncio

import disnake
from disnake.ext import commands
from transformers import pipeline
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

list_channel_id = [int(id) for id in os.environ.get("CHANNEL_ID").split(",")]

# Setting the AI
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
model = "SamLowe/roberta-base-go_emotions"
classifier = pipeline("sentiment-analysis", model=model)

# Setting the Database
client = MongoClient(os.environ["MONGO_DB_URL"])
db = client[os.environ["DATABASE_NAME"]]
collection = db[os.environ["COLLECTION_NAME"]]


# Making the Database insertion asynchronous
async def insert_data(data: dict) -> None:
    print(data)
    await asyncio.to_thread(collection.insert_one, data)
    print("!!!")


# Setting the bot
intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return  # Ignore messages from the bot itself

    if ctx.channel.id in list_channel_id:

        # Getting the AI response
        message_emotion = classifier(ctx.content)

        # Sending the data to the database
        await insert_data({
            'message': {
                'message_id': ctx.id,
                'channel': {
                    'channel_name': str(ctx.channel),
                    'channel_id': int(ctx.channel.id)
                }
            },
            'time': datetime.datetime.now(tz=datetime.timezone.utc),
            'ai': {
                'label': message_emotion[0]['label'],
                'score': message_emotion[0]['score']
            }
        })


bot.run(os.environ["BOT_TOKEN"])
