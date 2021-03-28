#!/usr/bin/python3

# By @__MrHolmes

# Imports
import discord # pip3 install discord
import os
import dotenv # pip3 install python-dotenv
from discord.ext import commands
import time
import asyncio

# Edit the name of your base file
BASE_FILE = 'notifications.txt'
# Edit the delay you want between the check of notifications
DELAY = 1

# Function to read the base file and look for notifications
def notificationFile():
    with open(BASE_FILE,'r') as raw:
        return raw.readlines()[-1]
        

# Configuration 
TOKEN = dotenv.dotenv_values()['TOKEN']
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    if os.path.exists('notifications.txt'):
        os.system(f'mv {BASE_FILE} {BASE_FILE}.old && echo "Dummy notification" > {BASE_FILE}')

    print('System ready!')


@bot.command(name='notifications', help="Start the notification system")
async def notification(ctx):

    embed = discord.Embed(title=f"Initiated notification pipeline.", color=0x00ff40)

    msg = await ctx.channel.send(embed=embed)
    # Setting up check variable
    currNotifications = ''

    while True:
        # Getting newer notifications
        newerNotifications = notificationFile()  

        # Checking if there are any new notifications
        if newerNotifications != currNotifications: 
            # Sending the notification
            new_embed = discord.Embed(title=f"New notification!", color=0x00ff40) 
            new_embed.add_field(name=f"Message:", value=f"{newerNotifications}", inline=False)
            await ctx.channel.send(embed=new_embed)

            # Updating the last notification
            currNotifications = newerNotifications

        #Waiting for given time then checking again.
        await asyncio.sleep(DELAY) 

bot.run(TOKEN)