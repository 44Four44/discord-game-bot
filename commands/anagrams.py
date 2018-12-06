from setup import *
# Anagram game

@botA.command(pass_context=True)
async def anagrams(ctx, length):
    # Player is the user who called the command
    player = ctx.message.author
    print("It's {}'s time to play!".format(player.name))
    # Time limit for the player to type words
    time_limit = 60

    # Open words file to pick a random word
    # Number of words: 276643
    with open('/Users/EthanWang/discord-game-bot/data/words.txt', 'r') as file:
        words = file.readlines()

    # Pick starting word to be scrambled
    word = ""
    while len(word) != int(length):
        word = random.choice(words).rstrip()
    print("Word to be scrambled: " + word)

    # Get the letters of the word
    letters = list(word)
    random.shuffle(letters)

    # Instructions to start the game
    await botA.say("You have {}s to find the most words. Type 's' shuffle your letters. Get ready!\nStarting in:"
                   .format(time_limit))

    # Ready countdown
    for i in range(3):
        await botA.say(3 - i)
        time.sleep(1)
    await botA.say("Start!")

    # Message for scrambling letters
    interface = await botA.say("Your letters are: {}".format(' '.join(letters)))
    # Message for displaying previous word and the score / validity
    score_interface = await botA.say("____")

    # Player's total score depending on word length
    score = 0
    # Number of valid words and total words
    valid = 0
    total_words = 0
    # List of valid and invalid words
    valid_words = []
    invalid_words = []

    # 3 letters : 100 points
    # 4 letters : 400 points
    # 5 letters : 1200 points
    # 6 letters : 2000 points
    # 7 letters : 3200 points
    # 8 letters : 5000 points
    # 9 letters : 8000 points
    # ...
    points = [0, 0, 100, 400, 1200, 2000, 3200, 5000, 8000, 11000, 14000, 18000, 22000, 26000, 32000, 38000, 45000]

    # Start game time
    start = time.time()
    while time.time() - start < time_limit:
        sent = await botA.wait_for_message(timeout=start + time_limit - time.time(),
                                           author=player, channel=ctx.message.channel, content=None)
        # True if sent is not empty
        if sent:
            sent_word = str.upper(sent.content)
            if sent_word + "\n" in words and isAnagram(sent_word, word) and len(sent_word) > 2:
                # Calculate points and display point message
                point = points[len(sent_word) - 1]
                score += point
                await botA.edit_message(message=score_interface, new_content="{} :white_check_mark: +{}".
                                        format(sent_word, point))

                # Add word to valid words and update word counts
                valid += 1
                total_words += 1
                valid_words.append(sent_word)
            else:
                # Debugging
                print("\nInvalid word: " + sent_word)
                print(sent_word)
                print("Validity:")
                print(sent_word + "\n" in words)
                print("Using given letters:")
                print(isAnagram(sent_word, word))
                print("More than 2 letters: ")
                print(len(sent_word) > 2)

                # Calculate points and display point message
                await botA.edit_message(message=score_interface, new_content="{} :x:".format(sent_word))

                # Add word to invalid words and update word counts
                total_words += 1
                invalid_words.append("~~" + sent_word + "~~")

            print(sent_word)

    # Calculating score...
    await botA.say("Time's up! Calculating score . . .")

    """"
    # Calculate score
    for sent_word in sent_words:
        # Check if word is valid and is more than 2 letters
        if sent_word + "\n" in words and isAnagram(sent_word, word) and len(sent_word) > 2:
            # Add to score and valid words list
            score += points[len(sent_word) - 1]
            valid += 1
            valid_words.append(sent_word)
        else:
            # Debugging
            print("\nInvalid word: " + sent_word)
            print(sent_word)
            print("Validity:")
            print(sent_word + "\n" in words)
            print("Using given letters:")
            print(isAnagram(sent_word, word))
            print("More than 2 letters: ")
            print(len(sent_word) > 2)

            invalid_words.append("~~" + sent_word + "~~")


    """

    # Sort valid and invalid lists
    valid_words.sort()
    valid_words.sort(key=len, reverse=True)
    invalid_words.sort()
    invalid_words.sort(key=len, reverse=True)


    # Display end game statistics
    await botA.say("Number of valid words: {} / {}\nTotal Score : {}".format(valid, total_words, score))
    await botA.say("Your words :\n{}\n{}".format('\n'.join(valid_words), '\n'.join(invalid_words)))

# Check if a word can be made with letters of another word
def isAnagram(small, big):
    for letter in small:
        if small.count(letter) > big.count(letter):
            return False
    return True
