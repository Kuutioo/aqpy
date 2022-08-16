class Item:
    def __init__(self, id, name, category, item_count):
        self.id = id
        self.name = name
        self.category = category
        self.item_count = item_count
        
    def add_item_count(self, count):
        self.item_count += count
        print(f'Added {count} quest item. Total count: {self.item_count}')
        
    def add_item_command(self):
        return '"addItems","items":{"' + str(self.id) + '"'