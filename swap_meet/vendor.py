class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = [item for item in inventory]
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        result = [item for item in self.inventory if item.category is category]
        return result

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item in self.inventory and
                their_item in other_vendor.inventory):
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
        else:
            return False
        return True
    
    # def get_items(self):
    #     return self.inventory

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first = self.inventory[0]
            self.remove(my_first)
            their_first = other_vendor.inventory[0]
            other_vendor.remove(their_first)
            self.add(their_first)
            other_vendor.add(my_first)
        return True
        
