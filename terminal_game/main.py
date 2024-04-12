from characters import *
from movement import *

antagonist = Hero("Owen")

print(antagonist.name)
print(f"Player starting position is ({antagonist.position_x}, {antagonist.position_y})")

move_north(antagonist)
print(f"{antagonist.name} is now at ({antagonist.position_x}, {antagonist.position_y})")

move_east(antagonist)
print(f"{antagonist.name} is now at ({antagonist.position_x}, {antagonist.position_y})")

move_south_west(antagonist)
print(f"{antagonist.name} is now at ({antagonist.position_x}, {antagonist.position_y})")