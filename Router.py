from collections import deque, namedtuple


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Router():
    def __init__(self):
        self.name               #string
<<<<<<< HEAD
        self.interface          #set of dict
        self.neighbors          #set of dict
=======
        self.interfaces          #set of dict
>>>>>>> f021137a446d095edead7b45ea64f7e9987fee0f
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


<<<<<<< HEAD

    def print_table(self):
        pass
    #end print_tabl
=======
    #end print_table
>>>>>>> f021137a446d095edead7b45ea64f7e9987fee0f
