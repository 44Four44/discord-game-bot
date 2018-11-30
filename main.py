#-----------------------------------------------------------------------------
# Name:        discord-game-bot
# Purpose:     Live playable game in discord
#
# Author:      Ethan Wang
# Created:     29-Nov-2018
# Updated:     29-Nov-2018
#-----------------------------------------------------------------------------

# Import functions
from commands.miscellaneous import *
from commands.snake import *

# Startup message
@bot.event
async def on_ready():
    print("My name is {} and I'm ready to play".format(bot.user.name))
    await bot.change_presence(game=discord.Game(name="Dota 2", type=1))

# Run bot in server
bot.run(TOKEN)