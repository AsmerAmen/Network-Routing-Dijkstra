from . import Router



class main():
    def __init__(self):
        self.devices = list()        #set of Router
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]
    #end __init__


    def add_router(self, _name, _interfaces):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _router = Router(_name, _interfaces)
        self.devices.append(_router)
    #end add_router

    def remove_router(self):
        pass
    #end remove_router


    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v

    def find_route(self, source, dest):

        q = queue.PriorityQueue()
        parents = []
        distances = []
        start_weight = float("inf")

        for i in graph.get_vertex():

            weight = start_weight
            if source == i:
                weight = 0
            distances.append(weight)
            parents.append(None)

        q.put(([0, source]))

        while not q.empty():
            v_tuple = q.get()
            v = v_tuple[1]

            for e in graph.get_edge(v):

                candidate_distance = distances[v] + e.weight
                if distances[e.vertex] > candidate_distance:

                    distances[e.vertex] = candidate_distance
                    parents[e.vertex] = v
                    # primitive but effective negative cycle detection
                    if candidate_distance < -1000:

                        raise Exception("Negative cycle detected")
                    q.put(([distances[e.vertex], e.vertex]))

        shortest_path = []
        end = dest
        while end is not None:

            shortest_path.append(end)
            end = parents[end]

        shortest_path.reverse()

        return shortest_path, distances[dest]
    #end find_route

    def refresh(self):
        pass
    #end refresh

    def add_end_user(self, _name, _interfaces):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _end_user = End_User(_name, _interfaces)
        self.devices.append(_end_user)
