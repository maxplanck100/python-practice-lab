class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        self.inventory[item] = self.inventory.get(item, 0) + quantity

    def remove_item(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
