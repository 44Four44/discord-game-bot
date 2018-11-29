from setup import *
# Miscellaneous commands for testing and fun purposes

@bot.command()
async def say(message):
    # Send a message to the general text channel
    await bot.send_message(discord.Object(id='515992928246824963'), message)
