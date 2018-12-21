from . import Router



class main():
    def __init__(self):
        self.routers = list()        #list of Router

    #end __init__


    def add_router(self, _name, _interfaces):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _router = Router(_name, _interfaces)
        self.routers.append(_router)

    #end add_router

    def remove_router(self):
        pass
    #end remove_router

    def find_route(self, source, dest):
        pass
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
