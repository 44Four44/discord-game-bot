from setup import *
# Basic snake game with arrow reactions as controls

@bot.command(pass_context=True)
async def snake(ctx):
    # Player is the user who called the command
    player = ctx.message.author

    # Coordinates of the snake's head
    xpos = 0
    ypos = 0

    # Message that will be edited to simulate the frames in the game
    interface = await bot.say("Coordinates = ({}, {})".format(xpos, ypos))

    # Add movement keys (arrow emoji reactions)
    emojis = ['◀', '🔼', '🔽', '▶']
    directions = [-1, 1, -1, 1]
    for direction in emojis:
        await bot.add_reaction(interface, direction)

    # Wait for controls
    while True:
        # The direction selected by the player
        control = await bot.wait_for_reaction(emoji=None, user=player, timeout=None, message=interface)
        arrow = control.reaction.emoji

        # Update coordinates
        index = emojis.index(arrow)
        if index == 0 or index == 3:
            xpos += directions[index]
        else:
            ypos += directions[index]

        # Edit message/game interface
        await bot.edit_message(interface, new_content=("Coordinates = ({}, {})".format(xpos, ypos)))
        
        # Reset reaction
        await bot.remove_reaction(interface, arrow, player)


