import getpass
def getWord():
        # ask the user for a word to play with
        print("(word will not show while typing)")
        return getpass.getpass(prompt="Enter a word to play with: ")

# draws the gallows and hangman depending on how many guesses the player has left
def drawGallows(guesses):
        
    if guesses == 6:
            print(
            "    ---------  \n"
            "    |       '  \n"
            "    |          \n"   
            "    |          \n"
            "    |          \n"
            "   / \         \n"
            )
    elif guesses == 5:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |          \n"
            "    |          \n"
            "   / \         \n"     
            )
    elif guesses == 4:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |       |  \n"
            "    |          \n"
            "   / \         \n"     
            )
    elif guesses == 3:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |       |\ \n"
            "    |          \n"
            "   / \         \n"     
            )
    elif guesses == 2:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |      /|\ \n"
            "    |          \n"
            "   / \         \n"     
            )
    elif guesses == 1:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |      /|\ \n"
            "    |      /   \n"
            "   / \         \n"     
            )
    elif guesses == 0:
                    print(
            "    ---------  \n"
            "    |       '  \n"
            "    |       O  \n"   
            "    |      /|\ \n"
            "    |      / \  \n"
            "   / \         \n"     
            )

def displayWordProgress(wordProgress):
        print(wordProgress)
        print("")


# initiallizing the game
word = getWord().upper()
# a string that shows the progress on the word
wordProgress = "_" * len(word)
# a list of all the guessed letters
guessedLetters = []
# set the number of guesses available (standard being 6)
guesses = 6
# a variable to determine if play is still happening
playing = 1

# the game loop
while playing == 1:
    drawGallows(guesses)
    displayWordProgress(wordProgress)
    print("Guess a letter or word: ")
    guess = input().upper()
    # if you have guesses left
    if guesses > 1:
        # if guess is a word
        if len(guess) > 1:
                # if guess is the correct word
            if guess == word:
                print("'" + word + "' is the word!")
                drawGallows(guesses)
                displayWordProgress(word)
                print("You win!")
                playing = 0
            # if guess is incorrect
            else:
                print("'" + guess + "' is not the word")
                guesses -= 1
        # if guess is a letter
        elif len(guess) == 1:
            # if letter has already been guessed    
            if guess in guessedLetters:
                    print("You already guessed the letter '" + guess + "'")    
            # if guess is in the word
            elif guess in word:
                print("'" + guess + "' is in the word!")
                # turn wordProgress into a list to change it
                progressList = list(wordProgress)
                checkMatches = [i for i, letter in enumerate(word) if letter == guess]
                for index in checkMatches:
                        progressList[index] = guess
                wordProgress = "".join(progressList)
                guessedLetters.append(guess)
                # check if word is complete
                if "_" not in wordProgress:
                        playing = 0
                        drawGallows(guesses)
                        displayWordProgress(wordProgress)
                        print("YOU WIN!")
            # if guess is not in the word
            else:
                print("'" + guess + "' is not in the word")
                guessedLetters.append(guess)
                guesses -= 1
        # if empty input
        else:
            print("Invalid input")
    # if out of guesses
    else:
        guesses -= 1
        drawGallows(guesses)
        print("out of guesses...")
        print("The Correct word was:")
        displayWordProgress(word)
        playing = 0
