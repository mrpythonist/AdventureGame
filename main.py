def start_game():
    print("Welcome to the adventure game!")
    print("You find yourself in a dark forest, and you have to find a way out.")
    print("What would you like to do?")
    print("1. Search for a path")
    print("2. Climb a tree to get a better view")
    print("3. Wait for help")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_path()
    elif choice == "2":
        climb_tree()
    elif choice == "3":
        wait_for_help()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def search_path():
    print("You start searching for a path and soon find a fork in the road.")
    print("Which path would you like to take?")
    print("1. Left path")
    print("2. Right path")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You choose the left path and soon come across a river. You're able to find a bridge and cross it safely.")
        end_game("You successfully find your way out of the forest!")
    elif choice == "2":
        print("You choose the right path and soon come across a bear. Unfortunately, you are not able to outrun it and the bear catches you.")
        end_game("You were killed by the bear.")
    else:
        print("Invalid choice. Please try again.")
        search_path()

def climb_tree():
    print("You climb a tree and are able to see a nearby town.")
    print("What would you like to do?")
    print("1. Climb down the tree and head towards the town")
    print("2. Stay in the tree and wait for help")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You climb down the tree and head towards the town. After a long walk, you finally reach the town and find help.")
        end_game("You successfully find your way out of the forest!")
    elif choice == "2":
        print("You stay in the tree, but no help comes. Eventually, you run out of food and water and die of starvation.")
        end_game("You died.")
    else:
        print("Invalid choice. Please try again.")
        climb_tree()

def wait_for_help():
    print("You decide to wait for help.")
    print("After a while, a search party comes and finds you.")
    end_game("You successfully find your way out of the forest!")

def end_game(message):
    print(message)
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again == "yes":
        start_game()
    else:
        print("Thank you for playing!")

start_game()
