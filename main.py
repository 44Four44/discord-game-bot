from commands.miscellaneous import *

@bot.event
async def on_ready():
    print("My name is " + bot.user.name)
    await bot.change_presence(game=discord.Game(name="Dota 2", type=1))

bot.run(TOKEN)