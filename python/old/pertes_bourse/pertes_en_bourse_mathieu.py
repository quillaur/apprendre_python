import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def dbg(*strings):
    print(*strings, file=sys.stderr, flush=True)

n = int(input())

max_loose = 0
max_value = 0

for i in input().split():
    v = int(i)
    if v < max_value:
        max_loose = max(max_loose, max_value -v)
    max_value = max(v, max_value)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(- max_loose))
 
