class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        instance_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, instance_first_item, other_vendor_first_item)

        return True

    def get_by_category(self, category):
        category_list = []

        for item in self.inventory:
            if category == item.get_category():
                category_list.append(item)
        
        return category_list

    def get_best_by_category(self, category):
        category_inventory = self.get_by_category(category)
        highest_condition_item = None
        highest_condition = 0

        if category_inventory == []:
            return None
        
        for item in category_inventory:
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_condition_item = item
        
        return highest_condition_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_item = self.get_best_by_category(their_priority)
        my_item = other_vendor.get_best_by_category(my_priority)

        if not (self.get_by_category(their_priority) and other_vendor.get_by_category(my_priority)):
            return False

        self.swap_items(other_vendor, their_item, my_item)
        return True




