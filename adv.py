from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 'n']

# Store entire map as graph dictionary
map_graph = {}

# State returns current room exits, we need to iterate through to create the grap and the perform dft or bft

# Pointers to commands:
current_room_id = player.current_room.id
current_room_exits = player.current_room.get_exits()


def player_travel_direction(direction):
    pass
# create basic dictionary for each room when visited


def room_vertex():
    room = {}
    for exit in current_room_exits:
        room[exit] = '?'
        map_graph[current_room_id] = room


room_vertex()

print(map_graph)
# Loop through map and build a graph:
while len(map_graph) < len(room_graph):
    break
# For simple Line map, it is simple n,n but the computer wouldn't know that

# We need set up our own
# { 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'} }


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)


# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
