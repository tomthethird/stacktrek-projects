from random import choice
from datetime import datetime

print("\nLet's play HANGMAN!")
text = input("\nType 'PLAY' to start the game.\nType 'RULES' to learn how to play.\n\n>>")

wins = 0
loses = 0

play = True
while play:

    lives = 10                 # Change this for number of attempts
    seconds_countdown = 5     # Change this to declare time limit

    while (text.lower()) != "play":
        if text.lower() == "rules":
            print("\nRULES:\nYou, the player, is the man who is about to be hanged.")
            print("Guess the secret word by typing one letter at a time.")
            print(f"You will be given {lives} attempts and {seconds_countdown} seconds to save your life.")
            print("Guess it right and be free... or you will be the hanging man. :(\n")
            text = input("Type 'PLAY' to start your execution.\n\n>>")
        elif text.lower() == "end":
            play = False
        else:
            print("\nInvalid text.")
            text = input("Type 'PLAY' / 'RULES'\n\n>>")

    print("\nLet's start the game.\n")

    wordlist = ["computer","programming","technology","python","operations","numbers","integers","tuple","loops","output","stacktrek","foundation"]
    word = choice(wordlist)

    wordletter_list = []

    currenttime = datetime.now()                  #timer
    timestamp = currenttime.timestamp()
    seconds_added = timestamp + seconds_countdown

    for i in range(1, (len(word)+1)):
        i = "*"
        wordletter_list.append(i)

    print(f"Your {seconds_countdown} seconds starts now.")
    print(f"Your word has {len(word)} letters.")

    while (lives != 0):
        if (datetime.now().timestamp()) <= seconds_added:

            remaining_seconds = seconds_added - (datetime.now().timestamp())
            secondsformat = datetime.fromtimestamp(remaining_seconds).strftime("%S")  #convert to readable seconds

            if "*" in wordletter_list:
                print(f"\n{wordletter_list}")

                if lives == 1:
                    print(f"\nYou have {lives} last attempt left.")
                else:
                    print(f"\nYou have {lives} attempts left.")

                print(f"{secondsformat} second/s left.")

                letter = input("\nGuess a letter.\n>>")
                letter = letter.lower()

                numletter = word.count(letter)
                char_position = 0
                if numletter > 1:
                    for char in word:
                        if char == letter:
                            wordletter_list[char_position] = letter
                        char_position += 1

                char_position = word.find(letter)

                if letter in wordletter_list:
                    print(f"\nYou already have letter {letter.upper()}.")
                    lives -= 1

                if char_position < 0:
                    print(f"\nLetter {letter.upper()} is not in the word.")
                    # print("Sorry! You lose 1 attempt.")
                    lives -= 1
                else:
                    wordletter_list[char_position] = letter

            else:
                if lives == 1:
                    print(f"\nThat was close! You guessed the word!\nYour word is {word.upper()}.")
                    print("You are free! :D\n")
                    seconds_added = 0
                    wins += 1

                else:
                    print(f"\nHooray! You guessed the word!\nYour word is {word.upper()}.")
                    print("You are saved from hanging. :D\n")
                    seconds_added = 0
                    wins += 1

        else:
            lives = 0

    if (lives == 0) and (int(secondsformat) <= 00):
        loses += 1
        print("\nTIME IS UP!")
        
    elif (lives == 0) and (wordletter_list.count("*") > 0):
        loses += 1
        print(f"\nYou lose!\nSorry, better luck in the afterlife. :(\n") 
        print("           *******.   ")
        print("       ***  //   ***. ")
        print("     // ===//=== //.  ")
        print("    //    //    //.   ")
        print("   //    //    //.    ")
        print("  //    //    //.     ")
        print("-----------------    ")
        
    print("    GAME OVER\n")
    
    print(f"SCORE: Wins {wins}: Loses {loses}")
    text = input("Play again? Type 'PLAY' to play again or 'END' to exit.\n\n>>")
    if text.lower() == "end":
        play = False