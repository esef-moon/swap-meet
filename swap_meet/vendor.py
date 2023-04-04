from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, id):
        #check to see if id of item is in inventory - if so, return item.
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        #if my item not in my inventory, 
        #or their item not in their inventory return false.
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        #add their item to self, my item to their inventory.
        self.add(their_item)
        other_vendor.add(my_item)

        #remove my item from my inventory, their item from their inventory.
        self.remove(my_item)
        other_vendor.remove(their_item)
        

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        swap_first = self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return swap_first
            
