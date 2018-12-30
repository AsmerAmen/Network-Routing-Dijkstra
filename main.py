from Router import Router
from Interfaces import Interface
from tkinter import *
from tkinter import ttk
from scrolling_area import Table
from Dijkstra import *
import csv, os


class main():
    def __init__(self):
        #Functionality
        self.devices = list()        #set of Router

        #GUI
        self.root = Tk()
        self.root.geometry("500x600")
        self.root.title('Routing')
        img= PhotoImage(file='pkt.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
        style = ttk.Style()
        style.theme_use('classic')
        photo = PhotoImage(file="pkt.png").subsample(15, 15)

        self.table = None

        ##Buttons
        new_router_button = ttk.Button(self.root, text='New Router', width=10, command=self.new_rotuer)
        new_router_button.grid(row=0, column=1)

        read_file_button = ttk.Button(self.root, text='Read file', width=10, command = self.read_file)
        read_file_button.grid(row=1, column=1)

        refresh_button = ttk.Button(self.root, text='Refresh', width=10, command = self.home_refresh)
        refresh_button.grid(row=2, column=1)

        graph_button = ttk.Button(self.root, text='SP', width=10, command = self.get_SP_Window)
        graph_button.grid(row=3, column=1)



        routing_table_button = ttk.Button(self.root, text='Routing Table', width=10, command = self.get_rounting_table)
        routing_table_button.grid(row=6, column=1)
        ##end Buttons

        routing_table_router_label = ttk.Label(self.root, text='Router name:')
        routing_table_router_label.grid(row=4, column=1)

        self.routing_table_router_entry = ttk.Entry(self.root, width=5)
        self.routing_table_router_entry.grid(row=5, column=1, columnspan=1)

        self.root.update()
        # self.root.wm_attributes('-topmost', 1)
        self.root.mainloop()
    #end __init__


    def home_refresh(self):
        self.table = Table(self.root,  ["Router", "Interface", "Network", "Destination", "cost"], column_minwidths=[None, None, None, None, None])
        self.table.grid(row=0, column=2, rowspan=8)

        for device in self.devices:
            dev_name = device.name
            for interface in device.interfaces:
                self.table.insert_row([dev_name, interface.name, interface.network, interface.neighbor, interface.cost])
    #end home_refresh

    def new_rotuer(self):
        router_window = Toplevel(self.root)
        self.router_window = router_window
        self.interfaces_list = list()

        # Add Router components
        router_name_label = ttk.Label(router_window, text='Router name:')
        router_name_label.grid(row=0, column=0)

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
    #end new_rotuer

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


    def find_route(self):
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        shortest_path, distance = dijkstra(self.graph, int(source), int(destination))
        print(shortest_path, distance)

        self.path_cost_value['text']=str(distance)
        path_string = ' '.join(str(element) for element in shortest_path)
        self.path_value['text']=path_string

        self.source_entry.delete(0, 'end')
        self.destination_entry.delete(0, 'end')
    # #end find_route

    def get_graph(self):
        lines = list()
        no_of_nodes = len(self.devices) + 1
        self.graph = GraphUndirectedWeighted(no_of_nodes)
        for device in self.devices:
            dev_name = device.name
            for interface in device.interfaces:
                lines.append([dev_name, interface.neighbor, interface.cost])
        for line in lines:
            self.graph.add_edge(int(line[0]), int(line[1]), int(line[2]))
            print(line)


    def get_SP_Window(self):
        self.get_graph()



        SP_window = Toplevel(self.root)
        self.SP_window = SP_window

        SP_window.title('Routing')

        ##Source
        source_label = ttk.Label(SP_window, text='Source:')
        source_label.grid(row=0, column=0)

        self.source_entry = ttk.Entry(SP_window, width=5)
        self.source_entry.grid(row=0, column=1, columnspan=1)
        ##end Source

        ##Destination
        destination_label = ttk.Label(SP_window, text='Destination:')
        destination_label.grid(row=0, column=2)

        self.destination_entry = ttk.Entry(SP_window, width=5)
        self.destination_entry.grid(row=0, column=3, columnspan=1)
        ##end Distance

        ##Path
        path_label = ttk.Label(SP_window, text='Path:')
        path_label.grid(row=1, column=0)

        self.path_value = ttk.Label(SP_window, text='path..')
        self.path_value.grid(row=1, column=1, columnspan=2)
        ##end Path

        ##Cost
        path_cost_label = ttk.Label(SP_window, text='Cost:')
        path_cost_label.grid(row=1, column=3)

        self.path_cost_value = ttk.Label(SP_window, text='')
        self.path_cost_value.grid(row=1, column=4, columnspan=1)
        ##end Cost

        SP_button = ttk.Button(SP_window, text='Find SP', width=10, command=self.find_route)
        SP_button.grid(row=0, column=5)


    #end get_graph


    def get_rounting_table(self):
        self.get_graph()

        source = self.routing_table_router_entry.get()
        for dev in self.devices:
            if str(source) == str(dev.name):
                source_object = dev

        routing_table_window = Toplevel(self.root)
        self.routing_table_window = routing_table_window
        window_title = 'Router ' + str(source) + ' Routing Table'
        routing_table_window.title(window_title)

        self.table = Table(routing_table_window,  ["Destination", "Path",  "Interface", "cost"], column_minwidths=[None, 100, None, 50])
        self.table.grid(row=0, column=2, rowspan=8)

        for device in self.devices:
            destination = device.name
            print(destination)
            shortest_path, distance = dijkstra(self.graph, int(source), int(destination))
            print(shortest_path, distance)
            path_string = ' '.join(str(element) for element in shortest_path)
            print(path_string)
            if distance == 0:
                path_string = '-'
                interface_name = '-'
            else:
                for interface in source_object.interfaces:
                    if str(interface.neighbor) == str(shortest_path[1]):
                        interface_name = interface.name

            self.table.insert_row([destination, path_string, interface_name, distance])
    #end get_rounting_table


    def add_end_user(self, _name, _interfaces):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _end_user = End_User(_name, _interfaces)
        self.devices.append(_end_user)
    #end add_end_user

    def read_file(self):
        file = os.path.dirname(os.path.abspath(__file__)) + "/routers.csv"

        interfaces = list()
        routers_set = set()
        file_rows = csv.reader(open(file, 'r',encoding='utf8',), delimiter=',', quotechar='|')
        for row in file_rows:
          router  = row[0]
          name    = row[1]
          neighbor= row[2]
          ip      = row[3]
          cost    = row[4]
          subnet  = row[5]

          interface = Interface(name, neighbor, ip, cost, subnet)
          #create list of routers without repeatitions
          routers_set.add(router)
          #assign each interface object to it's associated router name
          interfaces.append([router, interface])
        #end for

        # create dictionary to hold the interfaces of each router
        routers_dict = {}
        for rout in routers_set:
            routers_dict.update({rout : []})

        #add the interfaces to the list of the router
        for inter in interfaces:
            routers_dict[inter[0]].append(inter[1])

        #clear the program devices list
        del self.devices[:]
        #create routers
        for k, v in sorted(routers_dict.items()):
            router = Router(k, v)
            self.devices.append(router)


if __name__ == '__main__':
    main()
