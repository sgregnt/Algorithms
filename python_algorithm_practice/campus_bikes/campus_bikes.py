# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
# Each worker and bike is a 2D coordinate on this grid.
# Our goal is to assign a bike to each worker. Among the available bikes and workers,
# we choose the (worker, bike) pair
# with the shortest Manhattan distance between each other, and assign the bike to that worker.
# (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance,
# we choose the pair with
# the smallest worker index; if there are multiple ways to do that,
# we choose the pair with the smallest bike index).
# We repeat this process until there are no available workers.
# The Manhattan distance between two points p1 and p2 is
# Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
# Return a vector ans of length N, where ans[i]
# is the index (0-indexed) of the bike that the i-th worker is assigned to.


# for each worker distance to each bike
# we order by distance and we make the avaliable

import bisect

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
workers_hash = {}
bikes_hash = {}
distances = []

for w_i, worker in enumerate(workers):
    for b_i, bike in enumerate(bikes):
        bikes_hash[tuple(bike)] = True
        dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        #i = bisect.bisect_right(distances, (dist, b_i, w_i)) # this is slow
        distances.append((dist, b_i, w_i))

distances.sort()
distances.reverse()
n = len(workers)
assignments = [0-1] * len(workers)
a = 0

def do_assignment(workers_hash, bikes_hash, distances, a):

    if a == n:
        return

    dist, b_i, w_i = distances.pop()
    if not w_i in workers_hash and b_i not in bikes_hash:
        assignments[w_i] = b_i
        bikes_hash[b_i] = True
        workers_hash[w_i] = True
        a += 1
    do_assignment(workers_hash, bikes_hash, distances, a)

do_assignment(workers_hash, bikes_hash, distances, a)
print(assignments)


