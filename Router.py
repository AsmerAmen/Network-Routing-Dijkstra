#from collections import deque, namedtuple
import queue
from collections import namedtuple


Edge = namedtuple('Edge', ['vertex', 'weight'])

class Router():
    def __init__(self):
        self.name               #string
        self.neighbors          #set of dict
        self.interfaces          #set of dict
        self.table              #set of dict
    #end __init__
    pass



    def set_name(self,_name):
        self.name=name
        pass

    def set_interface(self,_interface):
        self.interface=interface
        pass



    def update_table(self):

        pass
    #end update_table


    def print_table(self):
        pass
    #end print_table
