class GeneralCounter:
    _counter = 0

    def __init__(self):
        print GeneralCounter._counter
        GeneralCounter._counter += 1
        self.id = GeneralCounter._counter 

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
