from helpers import click

class Item:
    def __init__(self, id: int, name: str, category: str, item_count: int):
        self.id = id
        self.name = name
        self.category = category
        self.item_count = item_count
        
    def add_item_count(self, count):
        self.item_count += count
        print(f'Added {count} {self.name}. Total count: {self.item_count}')
    
    def display_count(self, quantity):
        print(f'You have {quantity} {self.name}\n')
        
    def alert_drop(self):
        print(f'You have recieved drop {self.name}')
        self.accept_drop(1)
    
    def accept_drop(self, item_number):
        click(1100, 50 * item_number)