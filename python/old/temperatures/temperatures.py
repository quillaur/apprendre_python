import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
print("n:", n, file=sys.stderr, flush=True)

closest_0 = 100000
min_dist = 100000

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    print("t:", t, file=sys.stderr, flush=True)

    dist_t = abs(t)

    if min_dist > dist_t:
        closest_0 = t
        min_dist = dist_t
    
    elif min_dist == dist_t:
        closest_0 = min_dist


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if n > 0:
    print(f"{closest_0}")
else:
    print("0")