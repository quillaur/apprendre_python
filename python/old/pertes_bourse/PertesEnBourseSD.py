import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print("n : ", n, file=sys.stderr, flush=True)

list_v = []

for i in input().split():
    v = int(i)
    print("v : ", v, file=sys.stderr, flush=True)
    list_v.append(v)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
#max_diff = math.inf

def getMaxDrawDown(liste_l : list, index_l=0): # returns maxDrawDown and index of local minimum
    min_l = min(liste_l[index_l:])
    index_min_l = liste_l.index(min_l)
    list_l_max = liste_l[index_l:index_min_l+1]

    
    print(f"min_l : {min_l}, list_l_max :{list_l_max}, ", file=sys.stderr, flush=True)
    if list_l_max != []:
        max_l = max(list_l_max)
    else:
        max_l = min_l

    max_diff_l = -(max_l - min_l)
    return max_diff_l, index_min_l

index_min_f=-1
max_final = math.inf

for i in range(n):
    if list_v[index_min_f+1:] != []:
        max_diff_f, index_min_f = getMaxDrawDown(list_v,index_min_f + 1)
        print(f"{max_diff_f}, {index_min_f}", file=sys.stderr, flush=True)
        if max_final > max_diff_f:
            max_final = max_diff_f


print(max_final)
