from characters import *
from random import randint

def fight(player, enemy):
    print(f"You have encountered a {enemy.name}. Prepare yourself!")

    while player.health > 0 and enemy.health > 0:
        return

def encounter(player):
    event = randint(1, 20)
    if event == 1:
        chest = (0.3 * player.experience_to_level)
        print(f"You found a chest and gained {chest} experience!")
    elif event >= 15 and event <= 20:
        enemy = Goblin()
        fight(player, enemy)
    else:
        print("There is nothing of note here.")
    return