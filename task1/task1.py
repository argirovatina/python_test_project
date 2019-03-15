class GeneralCounter:

    def __init__(self, id=0):
        self.id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id + 1   
 
class Id:
    id = GeneralCounter()
 
class Account(Id):
    pass
 
class Vehicle(Id):
    pass
 
class Player(Account):
    def __init__(self):
        object_id_collector = self.id
 
class Bot(Account):
    def __init__(self):
        object_id_collector = self.id
 
class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.id

 
print Player().id, Player().id, Tank().id, Bot().id, Player().id
