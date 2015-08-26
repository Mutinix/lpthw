from sys import exit
from random import randint
 
def cellar_room():
        print "You are in the cellar. It is full of gold. How much do you take?"
       
        next = raw_input("> ")
        if next.isdigit():
                amount = int(next)
        else:
                game_over("That's not a number, silly. The ground eats you up.")
               
        if amount < 50:
                print "You managed to take", amount, "gold. Hurray, you win!"
                exit(0)
        else:
                print "You tried to take too much gold."
                dragon_battle()
               
def weapon_selection():
        print "You see a few weapons around the room."
        print "A mace, a bow and some arrows & an axe."
        print "Which one do you pick?"
               
        weapon_choice = raw_input("> ")
        if "mace" in weapon_choice:
                print "You decide to combat the dragon with a mace."
                print "You swing the mace and hit the dragon's head."
                game_over("You have slain the dragon. You escape the castle with all the gold.")
        elif "bow" in weapon_choice or "arrow" in weapon_choice:
                print "You decide to take up the bow."
                print "Your constant barrage of arrows is nothing more than an irritation to the dragon."
                game_over("Even Legolas couldn't kill a dragon with a bow! The dragon burns you to ashes.")
        elif "axe" in weapon_choice:
                print "AND MY AXE!"
                print "You channel Gimli's energy through you and slice the dragon's head off with a clean swipe."
                game_over("The dragon has been slain. You may now enjoy all the riches.")
        else:
                game_over("There's no such weapon. The dragon eats you whole.")
               
def dragon_battle():
        print "You must now face the dragon!"
        print "What do you do?"
        print "Do you run or do you stay and fight?"
       
        next = raw_input("> ")
        if "run" in next:
                print "Wise choice."
                game_over ("You run away from the dragon and escape the castle. You get nothing. Good day sir!")
        elif "fight" in next:
                weapon_selection()
        else:
                print "That makes no sense!"
                dragon_battle()
               
def throne_room():
        print "You are in the throne room."
        print "You see the king seated on the throne surrounded by his guards."
        print "The king asks you to entertain him."
        print "What do you do?"
       
        next = raw_input("> ")
        if "dance" in next:
                amount = randint(10, 49)
                game_over("The king finds your dance highly amusing. He gives you %i gold." % amount)
        elif "sing" in next:
                game_over("The king is not amused. The guards chop your head off.")
        else:
                print "The king did not enjoy your performance."
                print "But he gives you one more chance."
                print "If you win, you will walk away with all the gold."
                print "The guard throw you in the cellar."
                dragon_battle()
               
def game_over(reason = ""):
        print reason
        print "Game over."
        exit(0)
       
       
def start():
        print "\n-----CASTLE ADVENTURE-----\n"
        print "You are at the gate of a castle."
        print "To enter the castle, you must answer a riddle."
       
        print "What do you put in a toaster?"
        riddle_answer = raw_input("> ")
        if riddle_answer == "toast":
                print "No silly, that's what you get from the toaster."
                game_over("The guards feed you to the sharks.")
        elif riddle_answer == "bread":
                print "You are granted access to the castle."
                print "You see 2 doors. A door to your left and a door to your right."
                print "Which one do you take?"
               
                room_choice = raw_input("> ")
                if room_choice == "left":
                        cellar_room()
                elif room_choice == "right":
                        throne_room()
                else:
                        game_over("You run in to a wall and die.")
                       
        else:
                print "The guards are not amused at your attempts to con them."
                game_over("They slice your head off.")
               
start()