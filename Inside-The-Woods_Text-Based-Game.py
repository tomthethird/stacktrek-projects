from datetime import datetime, timedelta
from time import sleep
from random import choice

character1 = "BASILIO"
character2 = "SISA"
adjectives = ["ferocious", "wild", "vicious", "savage", "hungry", "deadly", "restless"]

print("\n                INSIDE THE WOODS")
print(" -----------------------------------------------") 

print("         I  N  S  I  D  E       T  H  E    ")
print("  ##   ##   ##  ###     ###   #####     ##### ")
print("   ## #### ## ##   ## ##   ## ##   ## ##     ")
print("   ####  #### ##   ## ##   ## ##   ##   ####")
print("    ##    ##  ##   ## ##   ## ##   ##      ##")
print("    ##    ##   ####    ####   #####   #####")
print(" -----------------------------------------------") 
print("               A Text-Based Game")



text = input("\nType 'START' to play.\n\n>>")

while text.lower() != "start":
    if text.lower() != "start":
        print("Invalid input.")
        text = input("\n>>")
print("")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("zzZ")
    sleep(1)
    delay -= 1
 
print("\nDreaming...\n")

delay = 2
while delay > 0:
    timer = timedelta(seconds = delay)
    print("...")
    sleep(1)
    delay -= 1
 
print("\nHelloooooo...\n")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("...")
    sleep(1)
    delay -= 1

name = input("\nHello, you, what is your name?\n\n>>")

# input confirmation - START
text = input(f"\nAre you sure your name is '{name.upper()}'?\n\n'YES' or 'NO'>>")
while text.lower() != "yes":
    if text.lower() != "yes":
        print("\nPlease enter your name.")
        name = input(">>")
        text = input(f"\nAre you sure your name is '{name.upper()}'?\n\n'YES' or 'NO'>>")
# input confirmation - END

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

print(f"\nHello, {name.upper()}, welcome to your dream paradise.")

gender = input("\nAre a boy or a girl?\n\n>>")

# input confirmation - START
text = input(f"\nAre you sure you're a '{gender.upper()}'?\n\n'YES' or 'NO'>>")
while text.lower() != "yes":
    if text.lower() != "yes":
        print("\nPlease enter your gender.")
        gender = input(">>")
        text = input(f"\nAre you sure you're a '{gender.upper()}'?\n\n'YES' or 'NO'>>")
# input confirmation - END

print(f"\nOkay, I see. So, you're a {gender.upper()}.\nMay I know what is your birth year?")

year = int(input(">>"))

# input confirmation - START
text = input(f"\nAre you sure you were born in '{year}'?\n\n'YES' or 'NO'>>")
while text.lower() != "yes":
    if text.lower() != "yes":
        print("\nPlease enter your birth year.")
        year = int(input(">>"))
        text = input(f"\nAre you sure you were born in '{year}'?\n\n'YES' or 'NO'>>")
# input confirmation - END

#look for Chinese Zodiac
if (year-2000) % 12 == 0:
    zodiac_main = "DRAGON"
elif (year-2000) % 12 == 1:
    zodiac_main = "SNAKE"
elif (year-2000) % 12 == 2:
    zodiac_main = "HORSE"
elif (year-2000) % 12 == 3:
    zodiac_main = "SHEEP"
elif (year-2000) % 12 == 4:
    zodiac_main = "MONKEY"
elif (year-2000) % 12 == 5:
    zodiac_main = "ROOSTER"
elif (year-2000) % 12 == 6:
    zodiac_main = "DOG"
elif (year-2000) % 12 == 7:
    zodiac_main = "BOAR"
elif (year-2000) % 12 == 8:
    zodiac_main = "RAT"
elif (year-2000) % 12 == 9:
    zodiac_main = "OX"
elif (year-2000) % 12 == 10:
    zodiac_main = "TIGER"
else:
    zodiac_main = "RABBIT"

print(f"\nSo you were born in {year} and it was the year of the {zodiac_main}.")
print("You must be very lucky! I hope you find it pleasurable here.\n")

zodiac_list = ["DRAGON", "SNAKE", "HORSE", "SHEEP", "MONKEY", "ROOSTER", "DOG", "BOAR", "RAT", "OX", "TIGER", "RABBIT"]
zodiac_position = zodiac_list.index(zodiac_main)
del zodiac_list[zodiac_position]


print("It was a pleasure meeting you.\n")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print("", end="\r")
    sleep(1)
    delay -= 1
    
delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("zzZ")
    sleep(1)
    delay -= 1

print("\nType 'WAKE' to wake up and get up your bed.")
print("Type 'ZZZ' to continue sleeping.")
text = input(">>")
print("")

#decision loop ----- END
while text.lower() != "wake":
    if text.lower() == "zzz":
        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print("zzZ")
            sleep(1)
            delay -= 1
        print("\nType 'WAKE' to wake up and get up your bed.")
        print("Type 'ZZZ' to continue sleeping.")
        text = input(">>")
        print("")
        
    else:
        print("Invalid input.")
        text = input("\n>>")
        print("")
#decision loop ----- END

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("Knock!")
    sleep(1)
    delay -= 1

print("\nIs anybody home?")

print("\nType 'OPEN' to open the door.")
print("or type 'IGNORE'.")
text = input(">>")
print("")

#decision loop ----- START
while text.lower() != "open":
    if text.lower() == "ignore":
        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print("zzZ")
            sleep(1)
            delay -= 1
        print("\nIs anybody home?")
        text = input("\nType 'OPEN' / 'IGNORE'\n>>")
        print("")
    else:
        print("Invalid input.")
        text = input("\n>>")
        print("")
#decision loop ----- END

print(f"Hello, my name is {character1}, I am lost. I have no where to go.")
print("Thank goodness! I saw your house in the middle of the woods.\n")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("", end="\r")
    sleep(1)
    delay -= 1

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("*gasp*")
    sleep(1)
    delay -= 1
    
print("\nCan you help me get out of the woods?")

print(f"\nType 'YES' to trust {character1}.")
print(f"Type 'NO' if you find {character1} suspicious.")
text = input(">>")
print("")

#decision loop ----- START
while text.lower() != "yes":
    if (text.lower() == "no") or (text.lower() != "okay"):
        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print("Hmmm...")
            sleep(1)
            delay -= 1
        print(f"\nMy friend and I were trailing through this forest, when suddenly, a {choice(zodiac_list)} appeared in front of us.\n\nWe ran and we got separated.")

        print(f"\nType 'INQUIRE' to ask about the friend.")
        text = input(">>")
        print("")

        dialogue = True
        while dialogue:
            if text.lower() == "inquire":
                delay = 2
                while delay > 0:
                    timer = timedelta(seconds = delay)
                    print("Hmmm...")
                    sleep(1)
                    delay -= 1
                print(f"\nMy friend's name is {character2}. I ran too fast and left {character2} behind. I don't know where {character2} is right now. I hope {character2} is okay.\n\nMaybe you can help me find {character2} too?")
                dialogue = False
            else:
                print("Invalid input.")
                text = input("\n>>")
                print("")

        print(f"\nType 'OKAY' to help {character1}.")
        print("Type 'NO' to be rude.")
        text = input(">>")

        dialogue = True
        while dialogue:
            if text.lower() == "no":
                print(f"\n(You closed the door and left {character1} outside.)\n")
                delay = 3
                while delay > 0:
                    timer = timedelta(seconds = delay)
                    print("Knock!")
                    sleep(1)
                    delay -= 1
                print("\nPlease I really need your help. Please help me.")
                print("\n(You open the door and inspect him.)")
                text = input("\nType 'OKAY'/ 'NO'>>")

            elif text.lower() == "okay":
                dialogue = False

            else:
                print("\nInvalid input.")
                text = input("\n>>")
                print("")
        print("")

    elif text.lower() == "okay":
        text = "yes"
    else:
        print("Invalid input.")
        text = input("\n>>")
        print("")
#decision loop ----- END

print("(You enter back to your house to get a weapon.)")
print("\n(Choose between an 'OLD KNIFE' or a 'SLINGSHOT')")

weapon = input("Type 'OLD KNIFE' / 'SLINGSHOT'\n\n>>")

#decision loop ----- START
weapon_attack = 0
dialogue = True
while dialogue:
    if weapon.lower() == "old knife":
        weapon_attack = 3
        print("\n(You choose the OLD KNIFE.)")

        dialogue = False
    elif weapon.lower() == "slingshot":
        weapon_attack = 2
        print("\n(You choose SLINGSHOT.)")

        dialogue = False
    else:
        print("Invalid input.")
        weapon = input("\nType 'OLD KNIFE' / 'SLINGSHOT'>>")
#decision loop ----- END

weapon = weapon.upper()

itemquantity = [5, 8, 10, 3, 5, 5, 8, 10, 12, 3, 5, 8, 10, 3, 5, 5, 8, 10, 3, 15]

food = choice(itemquantity)
print(f"\n(You and {character1} quickly packed {food} food items, a rope and a torch.)")
print("\nType 'PRAY' to continue.")
text = input(">>")

# input confirmation - START
dialogue = True
while dialogue:
    if text.lower() == "pray":
        print("\n(You say a little prayer.)")
        print("\nCome on! Let's go. The sun is setting.")
        dialogue = False
    else:
        print("Invalid input.")
        text = input("\nType 'PRAY'>>")

# input confirmation - END

print(f"\n(You go on with {character1} and start your adventure.)\n\n")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

pebbles = choice(itemquantity)
print("\n(You traverse through a rocky area and found pebbles great for slinghot.)")
print(f"\n(You picked {pebbles} pebbles and put them in your pocket.)")

if weapon == "OLD KNIFE":
    print("\nWhat are you planning with that pebbles? You didn't bring your slingshot.\n")
elif weapon == "SLINGSHOT":
    print("\nThat's great! You can now use your slingshot.\n")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print("", end="\r")
    sleep(1)
    delay -= 1
delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("...")
    sleep(1)
    delay -= 1

print(f"\nWaaaaaah!\n")

delay = 2
while delay > 0:
    timer = timedelta(seconds = delay)
    print("Help!")
    sleep(1)
    delay -= 1

enemy1 = choice(zodiac_list)
zodiac_position = zodiac_list.index(enemy1)
del zodiac_list[zodiac_position]

print(f"\nA {choice(adjectives)} {enemy1} showed up and ready to attack {character1}!")

print(f"\nChoose what to do?\nType 'FOOD' to give food and distract the {enemy1}.")
print(f"Type 'ATTACK' to fight.")
text = input(">>")

flipcoin = [1, 2]
enemy_life = 15
criticalhit = weapon_attack*2

dialogue = True
while dialogue:
    if text.lower() == "food" and food == 0:
        print("You don't have food to throw.")
        text = input("\nType 'ATTACK'>>")

    elif text.lower() == "food":
        print(f"\nYou have {food} food item/s.")
        print(f"You throw 1 to the {enemy1}.")
        print("\n**FLIP A COIN. Type '1' for head / '2' for tail.**")
        print("If the coin flip to your chosen side. Your attempt will be successful.")
        print("If not, you will lose your item.")

        coin = int(input("Type '1' = head / '2' = tail.\n>>"))
        if (choice(flipcoin)) != coin:
            print(f"\nYou fail. You lose your item.\nTry again.")
            food -= 1
            text = input("\nType 'FOOD' / ATTACK'>>")
        else:
            print(f"\n(The {enemy1} fell into your scheme and devour the food you threw.")
            dialogue = False
    elif text.lower() == "attack":
        print(f"\n(You use your {weapon} to attack the {enemy1}.)")

        print("\n**FLIP A COIN. Type '1' for head / '2' for tail.**")
        print("If the coin flip to your chosen side. You will blow a critical hit.")

        coin = int(input("Type '1' = head / '2' = tail.\n>>"))
        if (choice(flipcoin)) != coin:
            print(f"\nYou blow {weapon_attack} hits!")
            enemy_life -= weapon_attack
            if enemy_life <= 0:
                print(f"\nYou defeated the {enemy1}.")
                dialogue = False
                break
            text = input("\nType 'FOOD' / ATTACK'>>")
        else:
            print(f"\nYou blow a CRITICAL hit!")
            enemy_life -= criticalhit
            if enemy_life <= 0:
                print(f"\nYou defeated the {enemy1}.")
                dialogue = False
                break
            text = input("\nType 'FOOD' / ATTACK'>>")
    else:
        print("Invalid input.")
        text = input("\nType 'FOOD' / ATTACK'>>")

weapon_attack += 2

print("\n(You successsfully defeated the enemy.)")
print(f"\n(You go on with your journey inside the woods with {character1}.)")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

enemy2 = choice(zodiac_list)
zodiac_position = zodiac_list.index(enemy2)
del zodiac_list[zodiac_position]

print(f"\nLook! {character2} is up there on that tree. She must have escaped.\nBut the {choice(adjectives)} {enemy2} is just below her. What should we do?")

print(f"\nChoose what to do?\nType 'FOOD' to give food and distract the {enemy2}.")
print(f"Type 'ATTACK' to fight.")
text = input(">>")

flipcoin = [1, 2]
enemy_life = 25
criticalhit = weapon_attack*2

dialogue = True
while dialogue:
    if text.lower() == "food" and food == 0:
        print("You don't have food to throw.")
        text = input("\nType 'ATTACK'>>")

    elif text.lower() == "food":
        print(f"\nYou have {food} food item/s.")
        print(f"You throw 1 to the {enemy2}.")
        print("\n**FLIP A COIN. Type '1' for head / '2' for tail.**")
        print("If the coin flip to your chosen side. Your attempt will be successful.")
        print("If not, you will lose your item.")

        coin = int(input("Type '1' = head / '2' = tail.\n>>"))
        if (choice(flipcoin)) != coin:
            print(f"\nYou fail. You lose your item.\nTry again.")
            food -= 1
            text = input("\nType 'FOOD' / ATTACK'>>")
        else:
            print(f"\n(The {enemy1} fell into your scheme and devour the food you threw.)")
            dialogue = False
    elif text.lower() == "attack":
        print(f"\n(You use your {weapon} to attack the {enemy2}.)")

        print("\n**FLIP A COIN. Type '1' for head / '2' for tail.**")
        print("If the coin flip to your chosen side. You will blow a critical hit.")

        coin = int(input("Type '1' = head / '2' = tail.\n>>"))
        if (choice(flipcoin)) != coin:
            print(f"\nYou blow {weapon_attack} hits!")
            enemy_life -= weapon_attack
            if enemy_life <= 0:
                print(f"\nYou defeated the {enemy2}.")
                dialogue = False
                break
            text = input("\nType 'FOOD' / ATTACK'>>")
        else:
            print(f"\nYou blow a CRITICAL hit!")
            enemy_life -= criticalhit
            if enemy_life <= 0:
                print(f"\nYou defeated the {enemy2}.")
                dialogue = False
                break
            text = input("\nType 'FOOD' / ATTACK'>>")
    else:
        print("Invalid input.")
        text = input("\nType 'FOOD' / ATTACK'>>")

weapon_attack += 2

print(f"\nThank you for saving me. I was so scared. It's good to see you again, {character1}.")
print("Who are you, by the way? But thank you for saving me.")

print(f"\n(You successsfully defeated the enemy and saved {character2}.)")
print(f"\n(You go on with your journey inside the woods with {character1} and {character2}.)\n")   

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

text = input("Type 'CONTINUE' to continue your journey.\n\n>>")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

print("\n(You continue to travel across the woods.)\n")

delay = 2
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

print("\n(The moon rises.)\n")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

print("\n(You sense something...)\n")

delay = 2
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

print("\n(A cold feeling.)\n")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("", end="\r")
    sleep(1)
    delay -= 1

Play = True

while Play:
    print(f"\nHey, {character1}! Are you okay? What's happening?\n")

    delay = 3
    while delay > 0:
        timer = timedelta(seconds = delay)
        print("Argh!")
        sleep(1)
        delay -= 1

    print("\nWAAAAAAAAHHHH!\n")

    delay = 1
    while delay > 0:
        timer = timedelta(seconds = delay)
        print("Argh!")
        sleep(1)
        delay -= 1

    print("\nWAAAAAAAAAAAAAAAAAAAAAAAAAAHHHH!\n")

    delay = 2
    while delay > 0:
        timer = timedelta(seconds = delay)
        print("Argh!")
        sleep(1)
        delay -= 1

    print("\nWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHH!\n")

    delay = 3
    while delay > 0:
        timer = timedelta(seconds = delay)
        print("...")
        sleep(1)
        delay -= 1

    main_adjective = choice(adjectives)
    print(f"\n({character1} tranformed into a {main_adjective} monster!)")
    print(f"\n{character2} is badly hurt.")
    print(f"\nHELP! Please! {name}, what's happening to {character1}?\nPlease save him!\n")

    delay = 3
    while delay > 0:
        timer = timedelta(seconds = delay)
        print("ARGH!")
        sleep(1)
        delay -= 1

    print(f"\nI am {character1}, the {main_adjective} {zodiac_main}! I am your zodiac!\nBe prepared to die!")

    print(f"\nType 'ATTACK' to fight the {zodiac_main}.")
    text = input(">>")

    
    numbergame = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    enemy_life = 60
    criticalhit = weapon_attack*4
    highhit = weapon_attack*2
    turns = 10

    while (turns != 0):
        if text.lower() == "attack":
            print(f"\n(You use your {weapon} to attack the {zodiac_main}.)")

            print("\n**PICK A NUMBER. Choose a number from '1' to '10'.**")
            print("You will blow a critical hit if guess the number, exactly.\nBlow high hits if it near the random number.")

            chosennumber = int(input("\nType a number from '1' to '10'\n>>"))
            luckynumber = choice(numbergame)
            if (chosennumber <1) or (chosennumber >10):
                print("\nInvalid input.)")
                text = input("\Type 'ATTACK'>>")

            elif luckynumber == chosennumber:
                print(f"\nYou blow a CRITICAL hit!")
                enemy_life -= criticalhit
                if enemy_life <= 0:
                    print(f"\nYou defeated the {zodiac_main}.")
                    break
                print(f"\nThe {zodiac_main} attacks you back. You received a damage.")
                turns -= 1
                text = input("\nType 'ATTACK'>>")

            elif ((luckynumber+1) == chosennumber) or ((luckynumber-1) == chosennumber):
                print(f"\nYou blow {highhit} hits!")
                enemy_life -= highhit
                if enemy_life <= 0:
                    print(f"\nYou defeated the {zodiac_main}.")
                    break
                print(f"\nThe {zodiac_main} attacks you back. You received a damage.")
                turns -= 1
                text = input("\nType 'ATTACK'>>")

            elif ((luckynumber+2) == chosennumber) or ((luckynumber-2) == chosennumber):
                print(f"\nYou blow {highhit-2} hits!")
                enemy_life -= highhit-2
                if enemy_life <= 0:
                    print(f"\nYou defeated the {zodiac_main}.")
                    break
                print(f"\nThe {zodiac_main} attacks you back. You received a damage.")
                turns -= 1
                text = input("\nType 'ATTACK'>>")

            elif ((luckynumber+3) == chosennumber) or ((luckynumber-3) == chosennumber):
                print(f"\nYou blow {highhit-3} hits!")
                enemy_life -= highhit-3
                if enemy_life <= 0:
                    print(f"\nYou defeated the {zodiac_main}.")
                    break
                print(f"\nThe {zodiac_main} attacks you back. You received a damage.")
                turns -= 1
                text = input("\nType 'ATTACK'>>")

            else:
                print(f"\nYou blow {weapon_attack} hits!")
                enemy_life -= weapon_attack
                if enemy_life <= 0:
                    print(f"\nYou defeated the {zodiac_main}.")
                    dialogue = False
                    break
                print(f"\nThe {zodiac_main} attacks you back. You received a damage.")
                turns -= 2
                text = input("\nType 'ATTACK'>>")
        else:
            print("\nInvalid input.")
            text = input("\n'Type 'ATTACK'>>")

    if turns == 0:
        print(f"\nYou lose!\n") 
        print("           *******.   ")
        print("       ***  //   ***. ")
        print("     // ===//=== //.  ")
        print("    //    //    //.   ")
        print("   //    //    //.    ")
        print("  //    //    //.     ")
        print("-----------------    ")
            
        print("    GAME OVER\n")

        dialogue = True
        text = input("Continue? Type 'ATTACK'\n\n>>")
        while dialogue:
            if text.lower() != 'attack':
                print("Invalid input.")
                text = input("Type 'ATTACK' to continue.\n\n>>")
            else:
                dialogue = False
    else:
        Play = False

        
print(f"\n(You successsfully defeated the {main_adjective} {zodiac_main} and brought {character1} back to normal.)\n")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print("...")
    sleep(1)
    delay -= 1

print(f"\nThen all of a sudden...\n")

delay = 8
while delay > 0:
    timer = timedelta(seconds = delay)
    print("...")
    sleep(1)
    delay -= 1

print(f"\nYou wake up from your dream.\n")
print("\nTHE END.\n\n")

delay = 5
while delay > 0:
    timer = timedelta(seconds = delay)
    print("", end="\r")
    sleep(1)
    delay -= 1

print("\n                INSIDE THE WOODS")
print(" -----------------------------------------------") 

print("         I  N  S  I  D  E       T  H  E    ")
print("  ##   ##   ##  ###     ###   #####     ##### ")
print("   ## #### ## ##   ## ##   ## ##   ## ##     ")
print("   ####  #### ##   ## ##   ## ##   ##   ####")
print("    ##    ##  ##   ## ##   ## ##   ##      ##")
print("    ##    ##   ####    ####   #####   #####")
print(" -----------------------------------------------") 
print("               A Text-Based Game")
print("              by TOMAS LOPEZ III\n\n")