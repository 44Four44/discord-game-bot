import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
import random
import math

# Token from pycharm environmental variable
TOKENA = os.environ['TOKENA']
TOKENB = os.environ['TOKENB']

# Initialize bots
botA = commands.Bot(command_prefix='$')
botB = commands.Bot(command_prefix='%')




