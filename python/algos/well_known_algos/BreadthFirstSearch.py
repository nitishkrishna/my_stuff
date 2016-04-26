"""
graph represented as an adjacency list
"""
from Queue import Queue

g = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


class BFS():

    def __init__(self):
        pass

    def breadth_first_search(self, graph, start_node):
        visited_nodes = set()
        to_visit_queue = Queue()
        to_visit_queue.put(start_node)
        while to_visit_queue.qsize() > 0:
            cur_vertex = to_visit_queue.get()
            if cur_vertex not in visited_nodes:
                neighbors = graph.get(cur_vertex, None)
                if neighbors:
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            to_visit_queue.put(neighbor)
                visited_nodes.add(cur_vertex)
        return visited_nodes


if __name__ == '__main__':
    bfs = BFS()
    v_nodes = bfs.breadth_first_search(g, 'A')
    print v_nodes
