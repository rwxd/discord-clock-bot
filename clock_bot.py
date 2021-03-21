from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
import pytz

load_dotenv()
token = getenv('TOKEN')
channel_id = getenv('CHANNEL_ID')

bot = commands.Bot(command_prefix='?')


def get_emoji(hour: str) -> str:
    pass


def get_time_string() -> str:
    tz = pytz.timezone('Europe/Berlin')
    time = datetime.now(tz).strftime('%H:%M:%S')
    return time


@ tasks.loop(seconds=60)
async def change_time() -> None:
    string = get_time_string()
    channel = bot.get_channel(int(channel_id))
    try:
        print(f'Chaning channel name to {string}')
        await channel.edit(name=string)
    except Exception as e:
        print(e)


@ bot.event
async def on_ready():
    change_time.start()
    print(f'Bot runs as {bot.user.name}')

bot.run(token)
