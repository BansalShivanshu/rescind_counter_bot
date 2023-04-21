import discord
from discord.ext import commands
import os

TOKEN = os.environ["TOKEN"]
bot = commands.Bot('^', token = TOKEN)

async def check_for_rescind(message):
    # check if the message contains rescind
    if 'rescind' in message.content.lower():
        # get the user data -- username     count
        # increment
        # save
        pass

# define command behaviour
@bot.command
async def count(ctx, user: commands.MemberConverter):
    # Get the user's 'rescind' counter from a database or file
    # Send a message to the channel with the user's counter
    # await ctx.send(f"{user.mention}, your rescind count is {counter}.")

# listen for incoming messages
@bot.event
async def on_message(message):
    await check_for_rescind(message)
    await bot.process_commands(commands)