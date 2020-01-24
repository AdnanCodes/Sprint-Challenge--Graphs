import random
from ast import literal_eval
from player import Player
from room import Room
from world import World

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Store entire map as graph dictionary
map_graph = {}

# State returns current room exits, we need to iterate through to create the grap and the perform dft or bft

# Pointers to commands:
current_room_id = player.current_room.id
current_room_exits = player.current_room.get_exits()


def player_travel_direction(direction):
    return player.travel(direction)


# create basic dictionary for each room when visited
def current_room_vertex():
    room = {}
    for exit in current_room_exits:
        room[exit] = "?"
        map_graph[current_room_id] = room


# Algorithm to find random exit that hasn't been explored yet
def current_room_unexplored_exit():
    # Track the unexplored exits
    unexplored = []
    # find the exits in a current room
    for exit in current_room_exits:
        # Check whether given exits is has '?" for being unexplored
        if map_graph[current_room_id][exit] == "?":
            unexplored.append(exit)

    # Randomize the choice from unexplored exits and return as a string
    return random.choice(unexplored)


# Initialize the map graph building at first location
current_room_vertex()
print(f"Map Started {map_graph}")
# Loop through map and build a graph, check against given size from room_graph
while len(map_graph) < len(room_graph):
    break  # Break the loop for testing purposes
    '''
    We have two possibilities, we need to go down the path of rooms which have ?
    And we need to go back via BFS to find next unexplored room, while doing so we find out room id and attach it 
    '''
    # Player object contains move commands linking to Room object and current room is stored in player
    # Check inside of map_graph for current room, find where given room still have '?' exits remaining
    if map_graph[current_room_id].values().count('?') != 0:
        # do traversal in random direction
        pass
    else:
        # Do BFT to find nearest room with '?'
        # Room Path inside of BFT should hold room_id, this can be used to create the edges between rooms. Thus completing the graph.
        pass

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
