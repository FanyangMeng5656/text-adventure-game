from random import randint

def game_over():
    print("Game Over! You failed.")
    exit()

def win_game():
    print("Congratulations! You completed the Hogwarts challenge!")
    exit()

def great_hall(has_wand, has_cloak, beat_troll):
    print("\nYou're in the Great Hall.")
    print("Actions:")
    print("- go to classroom")
    print("- go to lake")
    
    if has_wand and not has_cloak:
        print("- go to secret room")
    if has_wand and has_cloak and not beat_troll:
        print("- go to forest")
    if beat_troll:
        print("- go to headmaster (win)")
    
    choice = input("What do you do? ").lower()
    
    if choice == "go to classroom":
        classroom(has_wand, has_cloak, beat_troll)
    elif choice == "go to lake":
        lake(has_wand, has_cloak, beat_troll)
    elif choice == "go to secret room" and has_wand and not has_cloak:
        secret_room(has_wand, has_cloak, beat_troll)
    elif choice == "go to forest" and has_wand and has_cloak and not beat_troll:
        forest(has_wand, has_cloak, beat_troll)
    elif choice == "go to headmaster" and beat_troll:
        win_game()
    else:
        print("Can't do that!")
        great_hall(has_wand, has_cloak, beat_troll)

def classroom(has_wand, has_cloak, beat_troll):
    print("\nYou're in the classroom.")
    
    if not has_wand:
        print("Professor gives you a wand!")
        has_wand = True
    
    print("\nActions:")
    print("- go back")
    
    choice = input("What do you do? ").lower()
    
    if choice == "go back":
        great_hall(has_wand, has_cloak, beat_troll)
    else:
        print("Can't do that!")
        classroom(has_wand, has_cloak, beat_troll)

def lake(has_wand, has_cloak, beat_troll):
    print("\nYou're by the black lake.")
    
    if not has_cloak:
        print("You see a shiny cloak!")
    
    print("\nActions:")
    print("- go back")
    if not has_cloak:
        print("- take cloak")
    
    choice = input("What do you do? ").lower()
    
    if choice == "go back":
        great_hall(has_wand, has_cloak, beat_troll)
    elif choice == "take cloak" and not has_cloak:
        print("You took the cloak!")
        has_cloak = True
        great_hall(has_wand, has_cloak, beat_troll)
    else:
        print("Can't do that!")
        lake(has_wand, has_cloak, beat_troll)

def secret_room(has_wand, has_cloak, beat_troll):
    print("\nYou're in a secret room.")
    print("Answer the riddle:")
    print("What gets bigger when you share it?")
    
    answer = input("Your answer: ").lower()
    
    if answer == "happiness":
        print("Correct! You may proceed.")
    else:
        print("Wrong! Try again.")
    
    great_hall(has_wand, has_cloak, beat_troll)

def forest(has_wand, has_cloak, beat_troll):
    print("\nYou're in the dark forest.")
    print("A troll attacks you!")
    
    print("\nActions:")
    print("- fight")
    print("- run")
    
    choice = input("What do you do? ").lower()
    
    if choice == "fight":
        print("You used your wand and beat the troll!")
        beat_troll = True
    elif choice == "run":
        game_over()
    else:
        print("Can't do that!")
    
    great_hall(has_wand, has_cloak, beat_troll)

# Start game
print("Welcome to Hogwarts Adventure!")
print("Get a wand, find the cloak, beat the troll, and win!")
great_hall(False, False, False)
