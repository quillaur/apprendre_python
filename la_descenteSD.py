import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.



# game loop
while True:

    l=[]
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        l.append(mountain_h)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    ####

    highest_mountain = max(l)

    highest_mountain_index = l.index(highest_mountain)


    # The index of the mountain to fire on.
    print(f"{highest_mountain}, {l}", file=sys.stderr, flush=True)

    print(highest_mountain_index)
