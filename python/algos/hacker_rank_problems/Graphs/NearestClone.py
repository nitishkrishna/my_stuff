#!/bin/python

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def BFS_dist(graph, u, v):
    q = [u]
    dist = {}
    dist[u] = {}
    dist[u][u] = 0
    while len(q):
        node = q[0]
        q = q[1:]
        nbrs = graph[node]
        if v in nbrs:
            dist[u][v] = dist[u][node] + 1
            return dist[u][v]
        else:
            for x in nbrs:
                dist[u][x] = dist[u][node] + 1
            q= q+nbrs
    
def find_clone(graph, nodes):
    min_dist = sys.maxsize
    dist = sys.maxsize
    
    for u in nodes:
        for v in nodes:
            if u == v:
                continue
            elif v in graph[u]:
                min_dist = 1
                return min_dist
            else:
                dist = BFS_dist(graph, u, v)
                if dist < min_dist:
                    min_dist = dist
    return min_dist

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    graph = {}
    col_graph = {}
    for n in range(0, graph_nodes):
        graph[n+1] = []
    for u in range(0, len(graph_from)):
        graph[graph_from[u]].append(graph_to[u])
        graph[graph_to[u]].append(graph_from[u])
    
    print graph
    for idx, col in enumerate(ids):
        if col not in col_graph:
            col_graph[col] = []
        col_graph[col].append(idx+1)
    
    if val not in col_graph or len(col_graph[val]) <=1:
        return -1
    else:
        return find_clone(graph, col_graph[val])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, raw_input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in xrange(graph_edges):
        graph_from[i], graph_to[i] = map(int, raw_input().split())

    ids = map(long, raw_input().rstrip().split())

    val = int(raw_input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

