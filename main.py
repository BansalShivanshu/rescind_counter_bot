import discord
from discord.ext import commands
import os

TOKEN = os.environ["TOKEN"]
bot = commands.Bot('^', token = TOKEN)

async def check_for_rescind(message):
    # check if the message contains rescind
    if 'rescind' in message.content.lower():
        
        pass