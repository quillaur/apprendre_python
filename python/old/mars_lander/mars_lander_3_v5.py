import sys
import math
from matplotlib.patches import Polygon
import numpy as np
import heapq

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


surface_n = int(input())  # the number of points used to draw the surface of Mars.
prev_y = -1
prev_x = -1
air_grid = [[0,2999]]
left_x = 0
right_x = 0

all_x = []
all_y = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    air_grid.append([land_x, land_y])
    all_x.append(land_x)
    all_y.append(land_y)

    if prev_y == land_y:
        target_x = prev_x + int((land_x - prev_x)/2)
        target_y = land_y
        left_x = prev_x
        right_x = land_x
    else:
        prev_y = land_y
        prev_x = land_x

print("x:", all_x, file=sys.stderr, flush=True)
print("y:", all_y, file=sys.stderr, flush=True)

air_grid.append([6999,2999])
p = Polygon(np.array(air_grid))

def valid_loc(id: tuple, p: Polygon) -> bool:
    return p.contains_point(id)

def get_neighbors(id: tuple, p: Polygon) -> list:
    x, y = id
    step = 100
    neighbors = [(x+step, y), (x-step, y), (x, y-step), (x, y+step)] # E W N S
    # results = filter(self.in_bounds, neighbors)
    results = [n for n in neighbors if valid_loc(n, p)]
    return results

def heuristic(a: tuple, b: tuple) -> float:
    return math.dist(a, b)

def find_shortest_path(grid, start, end):
    # Store exploration of the graph in another graph.
    dist = {start: [start]}
    cost_so_far = {start: 0}

    # which neighbor did I explore ?
    q = []
    heapq.heappush(q, (0, start))
    
    while len(q):
        # Where am I ?
        at = heapq.heappop(q)[1]

        for next in get_neighbors(at, grid):
            # I don't want to explore twice the same node.
            new_cost = cost_so_far[at] + 1
            if next not in dist or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, end)
                # How did I get there ?
                dist[next] = dist[at] + [next]
                # Add newly explored node to the list.
                heapq.heappush(q, (priority, next))
                
            
            # In our case, we don't need to explore the whole graph.
            if next == end or heuristic(at, end) < 150:
                q.clear()
                break

    return dist.get(next)

def get_main_points(path):
    main_p = path[0]
    main_points = []
    for p in path:
        x0, y0 = main_p
        x1, y1 = p

        if abs(y1 - y0) > 0 and math.dist(main_p, p) > 2000:
            main_p = prev_p
            main_points.append(main_p)

        prev_p = (x1,y1)
    main_points.append(prev_p)
    return main_points

path = []
target_power = None
target_rotate = None
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

    print("Actual position", x, y, file=sys.stderr, flush=True)

    if not path:
        start = (x, y)
        goal = (target_x, target_y)
        path = find_shortest_path(p, start, goal)
        main_points = get_main_points(path)

        print(main_points, file=sys.stderr, flush=True)
        main_x, main_y = main_points.pop(0)

    if x < main_x and main_points:
        main_x, main_y = main_points.pop(0)

    power = 4
    rotate = -20 if x < target_x else 20
    
    if main_x < x and main_y >= y:
        print("Target main point", file=sys.stderr, flush=True)
        if v_speed <= 0:
            power = 4
            rotate = 0
    
    elif left_x < x and abs(x - main_x) < 500:
        print("Top of cave", file=sys.stderr, flush=True)
        if v_speed <= 0:
            power = 4
            rotate = 0
    else:
        print("Slight descend", file=sys.stderr, flush=True)
        if v_speed > -15:
            power = 0
    
    if (x < target_x and h_speed > 40) or (x > target_x and h_speed < -40):
        rotate = -rotate
    
    if left_x < x < right_x and y - target_y < 1000:
        print("Landing...", file=sys.stderr, flush=True)
        if abs(h_speed) > 10:
            rotate = 60 if h_speed > 0 else -60
        else:
            rotate = 0
            if v_speed < -30:
                power = 4
            else:
                power = 0
        if y - target_y < 90:
            rotate = 0

    print(rotate, power)
