class Interface():
    def __init__(self, _name, _neighbor, _ip, _cost, _subnet):
        self.name       = _name         # str
        self.neighbor  = _neighbor    # str
        self.ip         = _ip           # string
        self.cost       = _cost         # int
        self.subnet     = _subnet       # string

        self.network = self.get_network()   # network dict
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
            octet = (int(_ip_octets[i]) & int(_subnet_octets[i]))
            _network_octets.insert(i,  str(octet))
        #end for

        _netowrk = _network_octets[0] + "." + _network_octets[1] + "." + _network_octets[2] + "." + _network_octets[3]

        return (_netowrk)
