# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot('!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def test(ctx):
    await ctx.send("Test")


@client.command()
async def craft(ctx):
    await ctx.send('Craft Bot')


@client.command()
randomNum=random.randint(1,2)
tailsNum=0
headsNum=0
async def coinflip(ctx, coinTimes=1):
    if coinTimes!=1:
        for i in range(min(max(times,1), 500)):
            if randomNum=1:
                headsNum+=1
            else:
                tailsNum+=1
            randomNum=random.randint(1,2)
     else:
        if randomNum=1:
            await ctx.send('You flipped Heads!')
        else:
            await ctx.send('You flipped Tails!')
   await ctx.send('You flipped Heads "+headsNum+" times and Tials "+tailsNum+" times!")


@client.command()
async def poll(ctx):
    upvote = '<:upvote:778439419014152193>'
    downvote = '<:downvote:778439419010613249>'

    await ctx.message.add_reaction(upvote)
    await ctx.message.add_reaction(downvote)


@client.command()
async def pizza(ctx):
    await ctx.send("Pizza")

@client.command()
async def mungeSpam(ctx, times=1):
    for i in range(min(max(times, 1), 10)):
        await ctx.send("@everyone munge")

client.run(TOKEN)
