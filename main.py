from Router import Router
from Interfaces import Interface
from tkinter import *
from tkinter import ttk
from scrolling_area import Table


class main():
    def __init__(self):
        #Functionality
        self.devices = list()        #set of Router
        # self.vertex_count = vertex_count
        # self.adjacency_list = [[] for _ in range(vertex_count)]


        #GUI
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title('Routing')
        img= PhotoImage(file='pkt.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        style = ttk.Style()
        style.theme_use('classic')

        photo = PhotoImage(file="pkt.png").subsample(15, 15)


        self.table = Table(self.root,  ["Router", "Interface", "Network", "Destination"], column_minwidths=[None, None, None, None])
        self.table.grid(row=0, column=2, rowspan=5)

        self.root.update()

        new_router_button = ttk.Button(self.root, text='New Router', width=10, command=self.new_rotuer)
        new_router_button.grid(row=0, column=1)

        refresh_button = ttk.Button(self.root, text='Refresh', width=10, command = self.home_refresh)
        refresh_button.grid(row=1, column=1)

        self.root.wm_attributes('-topmost', 1)
        self.root.mainloop()
    #end __init__


    def home_refresh(self):
        print(self.table.number_of_rows)
        for i in range(self.table.number_of_rows):
            self.table.delete_row(i+1) ## TODO: fix this shit

        for device in self.devices:
            dev_name = device.name
            for interface in device.interfaces:
                self.table.insert_row([dev_name, interface.name, interface.network, interface.neighbor])
        # self.table.set_data([[1,2,3],[4,5,6], [7,8,9], [10,11,12], [13,14,15],[15,16,18], [19,20,21]])
        # self.table.cell(0,0, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")
        #
        # self.table.insert_row([22,23,24])
        # self.table.insert_row([25,26,27])





<<<<<<< HEAD
    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e
=======
    def new_rotuer(self):
        router_window = Toplevel(self.root)
        self.router_window = router_window
        self.interfaces_list = list()

        # Add Router components
        router_name_label = ttk.Label(router_window, text='Router name:')
        router_name_label.grid(row=0, column=0)
>>>>>>> 133b874b35a0cf48d85b5af372782b82119c84c7

        self.router_name_entry = ttk.Entry(router_window, width=5)
        self.router_name_entry.grid(row=0, column=1, columnspan=1)

        add_router_button = ttk.Button(router_window, text='Add Router', width=10, command=self.add_router)
        add_router_button.grid(row=2, column=11)
        # end Add Router component


        # Add Interface components
        ##Name
        interface_name_label = ttk.Label(router_window, text='Name:')
        interface_name_label.grid(row=1, column=0)

        self.interface_name_entry = ttk.Entry(router_window, width=5)
        self.interface_name_entry.grid(row=1, column=1, columnspan=1)
        ##end Name

        ##Neighbour
        interface_neighbour_label = ttk.Label(router_window, text='Neighbour:')
        interface_neighbour_label.grid(row=1, column=3)

        self.interface_neighbour_entry = ttk.Entry(router_window, width=5)
        self.interface_neighbour_entry.grid(row=1, column=4, columnspan=1)
        ##end Neighbour

        ##IP
        interface_ip_label = ttk.Label(router_window, text='IP:')
        interface_ip_label.grid(row=1, column=5)

        self.interface_ip_entry = ttk.Entry(router_window, width=15)
        self.interface_ip_entry.grid(row=1, column=6, columnspan=1)
        ##end IP

        ##Subnet
        interface_subnet_label = ttk.Label(router_window, text='Subnet mask:')
        interface_subnet_label.grid(row=1, column=7)

        self.interface_subnet_entry = ttk.Entry(router_window, width=15)
        self.interface_subnet_entry.grid(row=1, column=8, columnspan=1)
        ##end Subnet

        ##Cost
        interface_cost_label = ttk.Label(router_window, text='Cost:')
        interface_cost_label.grid(row=1, column=9)

        self.interface_cost_entry = ttk.Entry(router_window, width=5)
        self.interface_cost_entry.grid(row=1, column=10, columnspan=1)
        ##end Cost

        add_interface_button = ttk.Button(router_window, text='Add Interface', width=13, command=self.add_interface)
        add_interface_button.grid(row=1, column=11)
        #end Add Interface components



    def new_interface(self):
        pass

    def add_router(self):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _name = self.router_name_entry.get()
        _interfaces = self.interfaces_list
        _router = Router(_name, _interfaces)
        self.devices.append(_router)
        self.router_window.destroy()
    #end add_router

    def add_interface(self):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        # Get User values from entries
        _name = self.interface_name_entry.get()
        _neighbour = self.interface_neighbour_entry.get()
        _ip = self.interface_ip_entry.get()
        _cost = self.interface_cost_entry.get()
        _subnet = self.interface_subnet_entry.get()

        # Clear entries
        self.interface_name_entry.delete(0, 'end')
        self.interface_neighbour_entry.delete(0, 'end')
        self.interface_ip_entry.delete(0, 'end')
        self.interface_cost_entry.delete(0, 'end')
        self.interface_subnet_entry.delete(0, 'end')

        _interface = Interface(_name, _neighbour, _ip, _cost, _subnet)
        self.interfaces_list.append(_interface)
    #end add_router

    def remove_router(self):
        pass
    #end remove_router


    # def get_edge(self, vertex):
    #     for e in self.adjacency_list[vertex]:
    #         yield e
    #
    # def get_vertex(self):
    #     for v in range(self.vertex_count):
    #         yield v

    # def find_route(self, source, dest):
    #
    #     q = queue.PriorityQueue()
    #     parents = []
    #     distances = []
    #     start_weight = float("inf")
    #
    #     for i in graph.get_vertex():
    #
    #         weight = start_weight
    #         if source == i:
    #             weight = 0
    #         distances.append(weight)
    #         parents.append(None)
    #
    #     q.put(([0, source]))
    #
    #     while not q.empty():
    #         v_tuple = q.get()
    #         v = v_tuple[1]
    #
    #         for e in graph.get_edge(v):
    #
    #             candidate_distance = distances[v] + e.weight
    #             if distances[e.vertex] > candidate_distance:
    #
    #                 distances[e.vertex] = candidate_distance
    #                 parents[e.vertex] = v
    #                 # primitive but effective negative cycle detection
    #                 if candidate_distance < -1000:
    #
    #                     raise Exception("Negative cycle detected")
    #                 q.put(([distances[e.vertex], e.vertex]))
    #
    #     shortest_path = []
    #     end = dest
    #     while end is not None:
    #
    #         shortest_path.append(end)
    #         end = parents[end]
    #
    #     shortest_path.reverse()
    #
    #     return shortest_path, distances[dest]
    # #end find_route

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


<<<<<<< HEAD


=======
>>>>>>> 133b874b35a0cf48d85b5af372782b82119c84c7
if __name__ == '__main__':
    main()
