from discord.ext import commands
import discord
import asyncio

bots = {}

def startbot(token):
    """
    Start a Discord bot

    Args:
        token (str): Bot's token
    """
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'Bot {bot.user} is online!')

    bots[token] = bot
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(token))

def stopbot(token):
    """
    Stop a discord Bot

    Args:
        token (str): Bot's token
    """
    if token in bots:
        bot = bots[token]
        loop = asyncio.get_event_loop()
        loop.create_task(bot.close())
        del bots[token]
