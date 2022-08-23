class Item:
    def __init__(self, id: int, name: str, category: str, item_count: int):
        self.id = id
        self.name = name
        self.category = category
        self.item_count = item_count
        
    def add_item_count(self, count):
        self.item_count += count
        print(f'Added {count} {self.name}. Total count: {self.item_count}')
        
    def add_item_command(self):
        return "'addItems', 'items': {'" + str(self.id) + "'"
    
    def item_count_command(self, quantity):
        return self.add_item_command + ": {'iQtyNow': " + str(quantity)