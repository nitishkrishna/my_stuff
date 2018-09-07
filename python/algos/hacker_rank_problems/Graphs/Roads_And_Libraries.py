def dfs(node, city_map, covered, uncovered, c_road):
    # traverse from the city
    cost = 0
    nodes = [node]
    while len(nodes) > 0:
        city = nodes.pop()
        neighbors = city_map[city]
        for neighbor in neighbors:
            if neighbor in covered:
                continue
            cost += c_road
            uncovered.remove(neighbor)
            covered.add(neighbor)
            nodes.append(neighbor)
    return cost, covered, uncovered

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    city_map = {i: [] for i in range(1, n+1)}

    for road in cities:
        city_map[road[0]].append(road[1])
        city_map[road[1]].append(road[0])

    cost = 0
    covered = set()
    uncovered = set(range(1, n+1))

    while len(covered) < n:
        city = uncovered.pop()

        # build library in the city
        cost += c_lib
        covered.add(city)

        if c_lib > c_road:
            sub_cost, covered, uncovered = \
                    dfs(city, city_map, covered, uncovered, c_road)
            cost += sub_cost

    return cost
