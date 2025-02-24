from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0.0):
        super().__init__(id, condition)
        #set type to unknown or type if given
        self.type = type
    #override parent stringify to add the second portion of string."  
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. This is a {self.type} device."
    
    