from . import Router


class main():
    def __init__(self):
        self.routers = set()        #set of Router
    #end __init__


=======
    def add_router(self, _name, _interfaces):
        '''
            @param: name, string
            @param: interfaces, set of Interface objects
        '''
        _router = Router()
        _router.set_name(_name)
        _router.set_interfaces(_interfaces)
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
        _end_user = End_User()
        _end_user.set_name(_name)
        _end_user.set_interfaces(_interfaces)
>>>>>>> f021137a446d095edead7b45ea64f7e9987fee0f
