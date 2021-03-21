from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv('TOKEN')
channel_name = getenv('CHANNEL_NAME')

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f'Bot runs as {bot.user.name}')


bot.run(token)
