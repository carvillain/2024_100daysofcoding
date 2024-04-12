from characters import *
from movement import *
from combat import *

if __name__ == "__main__":
    hero_name = input("Please let the world know your name traveler ")
    antagonist = Hero(hero_name)
    print(f"Welcome into the fold {antagonist.name}! Beware there are monsters in the area.")
    playing = True

    while antagonist.health > 0:
        action = input("What would you like to do? Move or heal ")

        if action.lower() == "heal":
            antagonist.heal()
        elif action.lower() == "move":
            direction = input("Which way are you going? (N, S, W, E, NE, NW, SE, SW) ")

            if direction.lower() == "n":
                move_north(antagonist)
            elif direction.lower() == "s":
                move_south(antagonist)

            print(f"You walk until you arrive at ({antagonist.position_x}, {antagonist.position_y})")
            encounter(antagonist)
        else:
            print("I am sorry. I didn't understand you.")

        





