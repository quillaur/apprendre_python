import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print("n:", n, file=sys.stderr, flush=True)

list_v = []
for i in input().split():
    v = int(i)
    print("v:", v, file=sys.stderr, flush=True)
    list_v.append(v)


max_diff = 100000
differences = []

for _ in range(len(list_v)):
    if list_v:
        min_v = min(list_v)
        index_min = list_v.index(min_v)

        if index_min == 0:
            max_diff = 0

        else:
            sub_list_v = list_v[:index_min]
            max_v = max(sub_list_v)
            max_diff = max_v - min_v
        
        differences.append(max_diff)

        list_v = list_v[index_min+1:]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print("diff:", differences, file=sys.stderr, flush=True)
max_diff = max(differences)
if max_diff:
    print(f"-{max_diff}")
else:
    print("0")
