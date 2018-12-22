#from collections import deque, namedtuple
import queue
from collections import namedtuple


Edge = namedtuple('Edge', ['vertex', 'weight'])

Routing_Table_scheme={

    "interf_name"   : None,   #interface name : string
    "connected"     : None,     #if router is directly connected :bool
    "_interface"    : None,     #interface : interface object no printed
    "subnet"        : None,
    "network"       : None,     #interface network : string
    "cost"          : None,     #interface cost : int
    "router"        : None,     #router name : string
}

class Router():
    def __init__(self, _name, _interfaces):
        self.name       = _name              #string
        self.interfaces = _interfaces         #list of dict
        self.neighbors = list()                 #list of dict

        self.table = list()              #list of dict
        self.create_table()
        print(self.name)
        for interface in self.interfaces:
            print(interface.name + interface.network)
    #end __init__



    def get_name(name):
        return self.name
    #end get_name

    def get_interfaces(self):
        return self.interface
    #get_interfaces



    def create_table(self):
        for interface in self.interfaces:
            _table_row = {
            "interf_name"   : interface.name,   #interface name : string
            "connected"     : True,     #if router is directly connected :bool
            "_interface"    : interface,     #interface : interface object no printed
            "network"       : interface.network,     #interface network : string
            "subnet"        : interface.subnet,
            "cost"          : interface.cost,     #interface cost : int
            "router"        : interface.neighbor,     #router name : string
            }
            self.table.append(_table_row)
    #end update_table

    def update_table(self):

        pass

    def know_neighbors(self):
        for interface in self.interfaces:
            self.neighbors.append(interface.neighbor)



    def print_table(self):
        for interface in self.interfaces:
            for k, v in interface:
                print(k +" : "+ v)
            print("==============================================")
    #end print_table
