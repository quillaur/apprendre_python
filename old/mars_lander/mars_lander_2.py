import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
prev_y = -1
prev_x = -1
mid_x = -1
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    if prev_y == land_y:
        left_x = prev_x
        right_x = land_x
        mid_x = prev_x + (land_x - left_x) / 2
    
    prev_x = land_x
    prev_y = land_y


print("mid:", mid_x, file=sys.stderr, flush=True)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Fly
    power = 4
    rotate = -20 if mid_x > x else 20  

    if abs(h_speed) > 40:
        rotate = 20 if h_speed > 0 else -20
    

    # Landing
    if x > left_x and x < right_x:
        print("Landing in progress...", file=sys.stderr, flush=True)
        if abs(h_speed) > 10:
            rotate = 60 if h_speed > 0 else -60
        
        else:
            rotate = 0
            if v_speed < -30:
                power = 4
            else:
                power = 0



    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(f"{rotate} {power}")
