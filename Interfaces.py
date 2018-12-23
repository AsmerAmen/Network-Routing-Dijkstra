

class Interface():
    def __init__(self, _name, _neighbour, _ip, _cost, _subnet):
        self.name       = _name         # str
        self.neighbour  = _neighbour    # str
        self.ip         = _ip           # string
        self.cost       = _cost         # int
        self.subnet     = _subnet       # string

        self.network = self.get_network()   # network dict

        #assert neighbour < vertex_count
        #assert dest < self.vertex_count
        #self.adjacency_list[nei].append(Edge(dest, weight))
        #self.adjacency_list[dest].append(Edge(source, weight))
    #end __init__

    def get_network(self):
        _ip_octets = list()
        _subnet_octets = list()
        _network_octets = list()
        for octet in self.ip.split('.'):
            _ip_octets.append(int(octet))
        #end for
        for octet in self.subnet.split('.'):
            _subnet_octets.append(int(octet))
        #end for

        for i in range(len(_subnet_octets)):
            _network_octets.insert(i, (bin(_ip_octets[i])[2:]) and (bin(_subnet_octets[i])[2:]))
        #end for
        _netowrk = _network_octets[0] + "." + _network_octets[1] + "." + _network_octets[2] + "." + _network_octets[3]
        return (_netowrk)

    def get_neighbour(self):
        return self.neighbour


    def get_cost(self):
        return self.cost
