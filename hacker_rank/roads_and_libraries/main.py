import math
import os
import random
import re
import sys

visited = []
adj = []
counter = 0


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    global visited, adj, counter
    visited = []
    adj = []

    # fill visited matrix
    for _ in range(n):
        visited.append(False)

    # init adjacency matrix
    zeros = []
    for _ in range(n):
        zeros.append(0)

    for _ in range(n):
        adj.append(zeros.copy())

    # Fill adjacency matrix
    # for vertex in cities:
    #     adj[vertex[0] - 1][vertex[1] - 1] = 1
    #     adj[vertex[1] - 1][vertex[0] - 1] = 1
    # print(adj)

    for vertex in cities:
        adj[vertex[0] - 1].append(vertex[1] - 1)
        adj[vertex[1] - 1].append(vertex[0] - 1)
    # for(int a1 = 0; a1 < m; a1++){
    #         int city_1 = in.nextInt();
    #         int city_2 = in.nextInt();
    #         adj.get(city_1 - 1).add(city_2 - 1);
    #         adj.get(city_2 - 1).add(city_1 - 1);
    # }

    # travel around graph
    cost = 0
    for i in range(n):
        if not visited[i]:
            counter = 0
            dfs(i)

            if c_lib > c_road:
                cost += c_lib + (c_road * (counter - 1))
            else:
                cost += c_lib * counter
    return cost


# def dfs(index):
#     global visited, counter, adj
#     visited[index] = True
#     counter += 1
#     row = adj[index]
#     for i in row:
#         if row[i] == 1 and not visited[i]:
#             dfs(i)

def dfs(index):
    global visited, counter, adj
    visited[index] = True
    counter += 1

    row = adj[index]
    for j in range(len(row)):
        if not visited[row[j]]:
            dfs(row[j])


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split(" ")

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
