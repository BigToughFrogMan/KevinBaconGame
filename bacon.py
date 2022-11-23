from bacon_pkg.lvl_structure import *
from bacon_pkg.flavor import *

title()
print("\n    You are a starving artist; an up and coming screenplay writer. Living in a malaise of coffee burn out, cigarettes to curb the hunger and the kind of loneliness that only comes with dedication to your craft; not to mention a regular dose of self deprecating narcissism. 'Hope' has been a word from a foreign language to you... until today!\n\nToday you woke up to a voicemail from a studio you had sent a copy of your 'Tremors Reboot' script to and they want to meet!")
while True:
    progress = 0
    turns = 0
    answer = input("\nWill you meet them?\n\n1. Yes\n2. No\nEnter: ")
    if answer == "2":
        break
    elif answer == "1":
        while True:
            if turns < 6:
                level_choice()
            else:
                no_more_turns()
                break
    else:
        print("\nInvalid Selection\n")
