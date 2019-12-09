jump_lookup = {}
graph = {}
lookup = {}


class Node(object):
    def __init__(self, key):
        self.key = key
        self.connections = []
        self.parent = None
        super().__init__()

    def add_orbit(self, node):
        self.connections.append(node)

    def traverse(self, total_orbits):
        if len(self.connections) == 0:
            return total_orbits
        dO = total_orbits
        for node in self.connections:
            dO += node.traverse(total_orbits + 1)
        return dO


def find_path(node1, node2, jumps):
    if node1 == node2:
        return jumps
    else:
        if jump_lookup.get(node1.key, None) is None:
            jump_lookup[node1.key] = jumps
        else:
            return jumps + jump_lookup.get(node1.key)
        if jump_lookup.get(node2.key, None) is None:
            jump_lookup[node2.key] = jumps
        else:
            return jumps + jump_lookup.get(node2.key)
        return find_path(node1.parent, node2.parent, jumps + 1)


def run():
    with open("6input.txt") as f:
        global graph, lookup
        for line in f:
            body, moon = line.strip().split(")")
            if lookup.get(body, None) is None:
                if lookup.get(moon, None) is None:
                    moon_node = Node(moon)
                else:
                    moon_node = lookup[moon]
                body_node = Node(body)
                body_node.add_orbit(moon_node)
                moon_node.parent = body_node
                graph[body] = body_node
                lookup[body] = body_node
                lookup[moon] = moon_node
            else:
                if lookup.get(moon, None) is None:
                    node = Node(moon)
                    lookup[body].add_orbit(node)
                    node.parent = lookup[body]
                    lookup[moon] = node
                else:
                    lookup[body].add_orbit(lookup[moon])
                    lookup[moon].parent = lookup[body]
        print(graph["COM"].traverse(0))
        print(find_path(lookup["YOU"].parent, lookup["SAN"].parent, 0))


run()
