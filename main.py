#-----------------------------------------------------------------------------
# Name:        discord-game-bot
# Purpose:     Live playable game in discord
#
# Author:      Ethan Wang
# Created:     29-Nov-2018
# Updated:     04-Dec-2018
#-----------------------------------------------------------------------------

# Import functions
from commands.miscellaneous import *
from commands.snake import *
from commands.anagrams import *

# Startup message
@botA.event
async def on_ready():
    print("My name is {} and I'm ready to play".format(botA.user.name))
    await botA.change_presence(game=discord.Game(name="Dota 1", type=1))

@botB.event
async def on_ready():
    print("My name is {} and I'm ready to play".format(botB.user.name))
    await botB.change_presence(game=discord.Game(name="Dota 2", type=1))

# Run bots in server
loop = asyncio.get_event_loop()
task1 = loop.create_task(botA.start(TOKENA))
task2 = loop.create_task(botB.start(TOKENB))
gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)