import discord
from discord.ext import commands
import os
import sqlite3

TOKEN = os.environ["TOKEN"]
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='^', intents=intents, token=TOKEN)

conn = sqlite3.connect('rescind_bot.db')
cursor = conn.cursor()

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
    pass

# listen for incoming messages
@bot.event
async def on_message(message):
    await check_for_rescind(message)
    await bot.process_commands(commands)

cursor.execute("SELECT COUNT(*) FROM rescind_counter WHERE name='Steve Jobs#9339';")
result = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM rescind_counter WHERE name='John Doe';")
result2 = cursor.fetchone()[0]

print(f'count for jobs: {result}\ncount for john doe: {result2}')

conn.close()