from setup import *
# Miscellaneous commands for testing and fun purposes

@botA.command()
async def say(message):
    # Send a message to the general text channel
    await botA.send_message(discord.Object(id='515992928246824963'), message)

@botB.command()
async def say(message):
    # Send a message to the general text channel
    await botB.send_message(discord.Object(id='515992928246824963'), message)
