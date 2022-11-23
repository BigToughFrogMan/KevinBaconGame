progress = 0
turns = 0
""" 
-----------------------------------------------------------------------------------
Level Functionality Functions
-----------------------------------------------------------------------------------
"""

#Function to require user to press a button to continue. It can be any button but for simplicity I ask them to press enter.

def next():
    input("\nENTER to continue\n")

#Function to quickly print a line empty

def space():
    print("\n")

#Function that ends the game on the user if they make a choice that is, relative to the other choices, very not related to Kevin Bacon or if they encountered an circumstantial hazard that killed them, jailed them or incapacitated them in some other form preventing them from continuing on.

def bad_choice():
    global turns
    global progress
    turns = 0
    progress = 0
    print("Loser! You will never make it in the film industry!\n")
    play_again()
    return progress, turns

#In this game you only have 6 turns. This function lets you know you ran out of turns and then offers to let you play again.

def no_more_turns():
    print("You did not find Kevin Bacon in time. The studio is rejecting your script.")
    play_again()

# This function happens at the end of every turn. It adds one to the variable turns and then prints your progress in turns and how many degrees of progress you have made.

def end_turn():
    global progress
    global turns
    turns += 1
    print("Total degrees of progress:", progress)
    print("\nYou have", 6 - turns, "turns left to find Kevin Bacon.")
    if turns == 6 and progress < 6:
        bad_choice()
    if progress >= 6:
        print("\nYou have made it to Kevin Bacon but he will never do another Tremors Movie. What were you even thinking?")
    return turns

# This function increments the ammount of progress the player has made towards finding Kevin Bacon

def prog(amt):
    global progress
    progress += amt
    if amt >= 1:
        print("You have gotten", amt, "degrees closer to Kevin Bacon")
    else:
        print("You have made no progress in finding Kevin Bacon and wasted some of what little time you have. Don't F$@k up again or you'll never make your screenplay a reality!")
    return progress

# Function that offers to let a player restart the game once they have died or lost. You have to reset all the arrays in addition to progress and turns in this function.

def play_again():
    global progress, turns, pictures, notes, phone, backpack
    print("Would you like to try again?")
    answer = input("1. Yes\n2. No\nEnter: ")
    if answer == "2":
        print("Quitting game...\n")
        quit()
    elif answer == "1":
        pictures = ["bathroom selfie", "bathroom selfie again", "picture of your mom" ]
        notes = ["bad poetry...", "grocery list...coffee, bagels, excedrin, fishsticks...etc"]
        contacts = {"Mom" : "703-488-9001", "Big Shot Studios" : "564-455-8910"}
        phone = (pictures, notes, contacts)
        backpack = ["'Tremors: In Space!' script", "half empty pint of whiskey", "pack of cigs", "phone charger"]
        progress = 0
        turns = 0
        level_choice()
    else:
        print("Invalid Selection")

#This is my main function that helps to decide whether to use template 1 or template 2 for the user level.

def level_choice():
    global progress
    global turns
    if progress == 0 and turns == 0:
        level0()
    elif progress in range(0, 5):
        level1()
    elif progress == 5:
        level2()
    elif progress == 6:
        print("\nYou have beaten '6 Degrees to Kevin Bacon'... Whoopee!\n")
        play_again()
    else:
        print("Game has encountered a bug and will terminate when you press enter")
        next()
        quit()

""" 
-----------------------------------------------------------------------------------
Character Items and Functions
-----------------------------------------------------------------------------------
"""
# a list that is pictures in your phone
pictures = ["bathroom selfie", "bathroom selfie again", "picture of your mom" ]

#notes you take in your phone, including clues to refer back to. You can also add notes as a user
notes = ["bad poetry...", "grocery list...coffee, bagels, excedrin, fishsticks..."]

#numbers in your phone relevant to the game
contacts = {"Mom" : "703-488-9001", "Big Shot Studios" : "564-455-8910"}

# You are given the option to access it at various times in the story It is a tuple that holds some lists and dictionaries
phone = (pictures, notes, contacts)

# a list that holds items the main character picks up along the way
backpack = ["'Tremors: In Space!' script", "half empty pint of whiskey", "pack of cigs", "phone charger"]

# This list will be unseen by the user but will be accessed to grant them access to different choices
keys = []

# view contents of backpack function... sometimes you could pick something up that will help you later
def open_backpack():
    print("\nOpening up your backpack...\n")
    for items in backpack:
        print(items)
    next()

# check phone function to view some useless stuff for flavor in addition to storing clues in photos, notes, and contacts
def check_phone():
    print("\nOpening your phone...\n")
    while True:
        phone_menu = input("1. Contacts\n2. Photos\n3. Notes\n4. Put phone away\nSelect Option: ")
        if phone_menu == "1":
            print("\nOpening contacts...\n")
            for contact, number in contacts.items():
                print(contact + ":" + number)
            next()
        elif phone_menu == "2":
            print("\nOpening photos...\n")
            for picture in pictures:
                print((int(pictures.index(picture))+1), ".", picture)
            next()
        elif phone_menu == "3":
            print("\nOpening notes...\n")
            for note in notes:
                print((int(notes.index(note))+1), ".", note)
            next()
            while True:
                note_menu = input("1. Create new note\n2. Delete note\n3. Back to menu\n")
                if note_menu == "1":
                    notes.append(input("Type your note here: \n\n"))
                    print("\nNote saved...\n")
                elif note_menu == "2":
                    for note in notes:
                        print((int(notes.index(note))+1), ".", note)
                    space()
                    while True:
                        try:
                            print("\nWhich note would you like to delete?\nEnter: ")
                            delete_note = int(input())
                            if len(notes) >= delete_note:
                                del notes[delete_note - 1]
                                print("\nNote deleting...")
                                print("\nNotes\n")
                                for note in notes:
                                    print((int(notes.index(note))+1), ".", note)
                                space()
                                break
                            else:
                                print("\nInvalid choice.\n")

                        except ValueError:
                            print("\nPlease enter your choice numerically.\n")
                elif note_menu == "3":
                    print("Returning to dashboard...\n")
                    break
        elif phone_menu == "4":
            print("Putting away phone...\n")
            break
        else:
            print("Invalid Selection")






"""
-----------------------------------------------------------------------------------
Level Functions
-----------------------------------------------------------------------------------
"""

#This will be a linked list. Each time a turn ends, a function will append a variable onto the tail of it. the level selector will have a parameter it calls for a function that checks what the last node was and assigns the corresponding level in the level_choice function. This will essentially build a one way map for the progress of the player. I have not built this section of code yet.


#First Level that Begins the Game
#This level only begins or is selected if turns and progress are at 0

def level0():
    global turns
    global progress
    turns = 0
    progress = 0
    space()
    print("======================================")
    print("~ ~ ~ ~ ~ ~BIG SHOT STUDIOS~ ~ ~ ~ ~ ~")
    print("======================================")
    print("\n    You just got out of the studio office with the big wigs from 'Big Shot Studios'. They said they loved your screenplay. There is only one problem. Those noodle heads only think it it'll work if you can get Kevin Bacon to sign on to reprise the role of Valentine.\n\nFortunately, being the mega fan that you are, you know exactly where he lives!")
    next()
    print("A short drive through the hollow plastic hills of Hollywood and 5 hours of your time later...")
    next()
    print("======================================")
    print("~ ~ ~ ~ ~KEVIN BACON'S HOUSE~ ~ ~ ~ ~ ")
    print("======================================")
    print("\nThe doorbell rings but no one is answering.")
    next()
    while True:
        answer = input("Ring again?\n1. Yes\n2. No\n")
        if answer == "1":
            print("\nStill no answer...")
            continue
        elif answer == "2":
            print("\nFrustrated, you lean against the railing of the porch, thinking... 'What to do?!?!'")
            next()
            print("With your head full of troubles, you barely notice as you knock a flower vase off the railing...!")
            next()
            print("You caught it! Close one...\nBut that gets you looking around and you notice the mailbox is overflowing, there's a ceramic pot on the ground that says 'For Graboids Only', and a welcome mat. Your detective hat is on now and you hear a sound coming from the backyard.")
            next()
            while True:
                print("1. Go around to the backyard\n2. Go through his mail\n3. Look inside the 'For Graboids Only' Pot\n4. Check under the welcome mat\n5. Check Your Phone\n6. Look in your backpack\n7. Leave")
                answer = input("\nWhat will you do?\nEnter: ")
                if answer == "1"and "hogwarts convention details" not in notes:
                    print("\nYou walk around back. The fence is too tall to see over but it looks like it isn't locked...")
                    next()
                    answer = input("What will you do?\n1. Enter the backyard\n2. Go back to front porch.\nEnter: ")
                    if answer == "1":
                        print("\nYou walk into the backyard but no one seems to be there. A pool has a bunch of empty PBR cans and a soggy pizza box floating in it... and there is a dog house with the name 'Digby' painted across the top.\n\nYou call out... 'Digby, come here boy!'")
                        print("but nothing stirs so you begin to make your way to the backdoor and the ground begins to shake...$%#$!!")
                        next()
                        print("The grass explodes right in front of you! Dirt flies everywhere and gets in your eyes and when you rub it away you see a... worm monster? A graboid! has burst from the earth and is poised right in front of you ready to strike!")
                        if "dog treats" in backpack:
                            next()
                            print("Without a thought you reach into your pocket for the dog treats you found in the pot and toss them at the beast. They land on the ground and the creature dives for them; swallowing them whole along with a sizable chunk of the yard.")
                            next()
                            print("Digby pops up out of the hole it dug and flops onto the yard and begins to wag it's 'tail?'.\n It's appetite appears to be satiated for now so you walk over to the backdoor and try to slide it open.")
                            next()
                            print("No luck! BUT!!! As you peer through the locked glass door you see a flyer for a Harry Potter Convention, and the time says its about to start! You pull your phone out and write down the name, time and venue of the event in your notes.\n")
                            backpack.remove("dog treats")
                            notes.append("hogwarts convention details")
                            keys.append("hogwarts")
                            answer = input(
                                "What do you do now?\n1. Head straight to the convention.\n2. Go back to front porch\nEnter: ")
                            if answer == "1":
                                print("\nStation 9 3/4 it is!")
                                prog(2)
                                end_turn()
                                next()
                                return progress, turns
                            if answer == "2":
                                continue
                        else:
                            next()
                            print("You begin to cry out as it leaps forward and wraps its maw around your legs. Conciousness flees from your mind and your vision begins to fade. The last thing you see is your lower half being swallowed by Kevin Bacon's pet graboid, Digby.\n\n You have died!\n")
                            bad_choice()
                            return
                    elif answer == "2":
                        print("\nYou head back...\n")
                    else:
                        print("Invalid selection.\n")
                elif answer == "2":
                    print("\nYou know you shouldn't go through his mail, but you are a degenerate so what the hell!")
                    next()
                    print("bills...coupons...taxes?...Half of these are open. It looks like he checked his mail then just stuffed them back in the box...")
                    next()
                    print("Bingo! Well not literally, but you find a reminder letter for jury duty summons. It looks like he should be in court right now!\n\nYou take a minute to write down the address in your phone's notes. Looks like it's a military court too...weird")
                    notes.append("jury duty at military court")
                    keys.append("goodmen")
                    next()
                elif answer == "3":
                    print("\nYou open up the lid of the jar. Inside you find dog treats. You shrug your shoulders, 'Why not' and put a few into your backpack.")
                    backpack.append("dog treats")
                    next()
                elif answer == "4":
                    print("\nWhen you lift up the welcome mat you don't find the key you were hoping for... but it's not like you were going to just walk into his house anyway right?...\n\nYou do find a business card and someone left a lipstick kiss on the back too!")
                    next()
                    print("                                                           ")
                    print(" /≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\ ")
                    print(" |                                                       | ")
                    print(" |    - - - - - - KELLERMAN'S DANCE CLUB - - - - - -     | ")
                    print(" |- - - - - - -Where the dancing gets dirty!- - - - - - -| ")
                    print(" |                                                       | ")
                    print(" |- - - - - - - - 42 Forest St. Hollywood- - - - - - - - | ")
                    print(" |                     623-559-0000                      | ")
                    print(" \≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈/ ")
                    print("                                                           ")
                    next()
                    pictures.append("Kellerman's Business Card")
                    backpack.append("Kellerman's Business Card")
                    keys.append("dd")
                    print("Might be worth checking out...\n")
                elif answer == "5":
                    check_phone()
                elif answer == "6":
                    open_backpack()
                elif answer == "7":
                    while True:
                        print("1. Go home and accept you are a failure")
                        if "hogwarts convention details" in notes:
                            print(str((keys.index("hogwarts")+2)) + ". Harry Potter Convention")
                        if "Kellerman's Business Card" in backpack:
                            print(str((keys.index("dd")+2)) + ". Kellerman's Dance Club")
                        if "jury duty at military court" in notes:
                            print(str((keys.index("goodmen")+2)) + ". Military Court")
                        break
                    while True:
                        answer = input("\nWhere do you want to go?\nEnter: ")
                        if answer == "1":
                            keys.clear()
                            bad_choice()
                        try:
                            if answer == str((keys.index("hogwarts")+2)) and "hogwarts" in keys:
                                print("\nStation 9 3/4 it is!")
                                keys.clear()
                                next()
                                prog(2)
                                end_turn()
                                return progress, turns
                        except: ValueError
                        try:
                            if answer == str((keys.index("dd")+2)) and "dd" in keys:
                                print("\nHope Kevin Bacon like's my spaghetti arms dance...")
                                keys.clear()
                                next()
                                prog(0)
                                end_turn()
                                return progress, turns
                        except: ValueError
                        try:
                            if "goodmen" in keys and answer == str((keys.index("goodmen")+2)):
                                print("\nmilitary courthouse... those facists better not have it guarded by men with guns!")
                                keys.clear()
                                next()
                                prog(1)
                                end_turn()
                                return progress, turns
                        except: ValueError
                        else:
                            print("\nInvalid Selection")
                            
                elif answer == "1" and "hogwarts convention details" in notes:
                    print("\nOn second thought, best not to risk another encounter with Digby the Graboid...")
                else:
                    print("Invalid Selection\n")
        else:
            print("Invalid Selection\n")

# Level 1 template offers three story choices. Each choice in addition to furthering the game adds or maintains the players current progress with a prog function. It also runs the end_turn function

def level1():
    print("level template 1")
    while True:
        choice = (input("option 1. 2. 3."))
        if choice == "1":
            prog(1)
            end_turn()
            return progress, turns
        elif choice == "2":
            prog(2)
            end_turn()
            return progress, turns
        elif choice == "3":
            prog(0)
            end_turn()
            return progress, turns
        else:
            print("invalid selection.")

# Level 2 template offers three story choices. Each choice in addition to furthering the game adds or maintains the players current progress with a prog function. It also runs the end_turn function. Level 2 switches the results of one option to run the bad_choice function which makes the player lose the game. Level 2 template is to be used when the player has reached progress of 5/6 one step away from Kevin Bacon.

def level2():
    print("level template 2")
    while True:
        choice = input("option 1. 2. 3.")
        if choice == "1":
            prog(1)
            end_turn()
            return progress, turns
        elif choice == "2":
            prog(0)
            end_turn()
            return progress, turns
        elif choice == "3":
            bad_choice()
            return
        else:
            print("invalid selection.")

