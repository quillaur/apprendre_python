import sys
import math
from collections import defaultdict, deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways


#######################
### GRAPH CREATION ####
#######################
# https://www.python.org/doc/essays/graphs/
graph = defaultdict(list)

n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)

#######################
### GRAPH EXITS #######
#######################
gates = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)

############
### BFS ####
############
def find_shortest_path(graph, start, end):
    # Store exploration of the graph in another graph.
    dist = {start: [start]}

    # which neighbor did I explore ?
    q = deque([start])
    while len(q):
        # Where am I ?
        at = q.popleft()
        print(at, graph[at], file=sys.stderr, flush=True)
        for next in graph[at]:
            # I don't want to explore twice the same node.
            if next not in dist:
                # How did I get there ?
                dist[next] = dist[at] + [next]
                # Add newly explored node to the list.
                q.append(next)
            
            # In our case, we don't need to explore the whole graph.
            if next == end:
                q.clear()
                break
        print("q:", q, file=sys.stderr, flush=True)
    return dist.get(end)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    print("si:", si, file=sys.stderr, flush=True)
    print("next:", graph[si], file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Look at each possible exit.
    min_dist = 1000
    shortest_p = []
    for g in gates:
        print("gate:", g, file=sys.stderr, flush=True)
        print("to gate:", graph[g], file=sys.stderr, flush=True)

        # Find the shorstest path between each exit and agent.
        path = find_shortest_path(graph, si, g)
        print("path:", path, file=sys.stderr, flush=True)

        # Select the smallest path the agent can take to exit.
        dist = len(path)
        if dist < min_dist:
            min_dist = dist
            shortest_p = path

    # Severe the first 2 nodes of the selected path.
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(f"{shortest_p[0]} {shortest_p[1]}")
