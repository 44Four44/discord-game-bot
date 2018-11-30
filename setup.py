import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
import random
import math

# Token from pycharm environmental variable
TOKEN = os.environ['TOKEN']

# Initialize bot
bot = commands.Bot(command_prefix='$')

