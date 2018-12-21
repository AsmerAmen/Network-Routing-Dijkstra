from collections import deque, namedtuple


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Router():
    def __init__(self):
        self.name               #string
        self.neighbors          #set of dict
        self.interfaces          #set of dict
        self.table              #set of dict
    #end __init__


    def set_name(name):
        self.name=name
        pass

    def set_interface(self):
        self.interface=interface
        pass



    def update_table(self):
        pass
    #end update_table


    def print_table(self):
        pass
    #end print_table
