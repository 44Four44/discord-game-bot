from setup import *
# Basic snake game with arrow reactions as controls

@botA.command(pass_context=True)
async def snake(ctx):
    # Player is the user who called the command
    player = ctx.message.author

    # Coordinates of the snake's head
    xpos = 10
    ypos = 10

    # Message that will be edited to simulate the frames in the game
    with open('/Users/EthanWang/discord-game-bot/interfaces/snake.txt', 'r') as file:
        data = file.readlines()
    plane = list(''.join(data))


    # Initial player position
    plane[41 * ypos + xpos] = '▓'

    # Display game interface and coordinates
    interface = await botA.say(''.join(plane))
    coordinates = await botA.say("Coordintes : ({}, {})".format(xpos, ypos))


    # Add movement keys (arrow emoji reactions)
    emojis = ['◀', '🔼', '🔽', '▶']

    for direction in emojis:
        await botA.add_reaction(interface, direction)

    # Frame count to switch between bots
    frame = 0
    bot = botA

    # Wait for controls
    while True:
        reaction = await botA.wait_for_reaction(emoji=None, user=player, timeout=None, message=interface)
        emojis = ['◀', '🔼', '🔽', '▶']
        directions = [-1, -1, 1, 1]

        # Delete position before update
        plane[41 * ypos + xpos] = '░'

        # Update coordinates
        print(reaction.reaction.emoji)
        index = emojis.index(reaction.reaction.emoji)

        if index == 0 or index == 3:
            xpos += directions[index]
        else:
            ypos += directions[index]

        # Edit message/game interface and coordinates message
        plane[41 * ypos + xpos] = '▓'

        await botA.edit_message(interface, new_content=(''.join(plane)))
        await botA.edit_message(coordinates, new_content=("Coordinates : ({}, {})".format(xpos, ypos)))

        # Reset user reaction
        await botA.remove_reaction(message=interface, emoji=reaction.reaction.emoji, member=player)

        # Next frame
        frame += 1