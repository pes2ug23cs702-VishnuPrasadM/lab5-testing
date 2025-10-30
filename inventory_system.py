"""Inventory management system for adding, removing, and saving stock data."""

import json
from datetime import datetime


class InventorySystem:
    """A class-based inventory management system."""

    def __init__(self, file_name="inventory.json"):
        """Initialize with a file name and empty stock data."""
        self.file_name = file_name
        self.stock_data = {}
        self.logs = []

    def add_item(self, item="default", qty=0):
        """Add a new item or update its quantity."""
        if not item:
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        self.logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove a quantity of an item from the stock."""
        if item not in self.stock_data:
            print(f"Item '{item}' not found in inventory.")
            return
        self.stock_data[item] -= qty
        if self.stock_data[item] <= 0:
            del self.stock_data[item]

    def get_qty(self, item):
        """Return the quantity of a specific item."""
        return self.stock_data.get(item, 0)

    def load_data(self):
        """Load stock data from a JSON file."""
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.stock_data = json.load(file)
        except FileNotFoundError:
            self.stock_data = {}

    def save_data(self):
        """Save current stock data to a JSON file."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.stock_data, file, indent=4)

    def print_data(self):
        """Print the current inventory report."""
        print("Items Report:")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """Return a list of items below a given threshold."""
        return [item for item, qty in self.stock_data.items() if qty < threshold]


def main():
    """Main function to run inventory operations."""
    system = InventorySystem()
    system.add_item("apple", 10)
    system.add_item("banana", -2)
    system.add_item("grapes", 5)
    system.remove_item("apple", 3)
    system.remove_item("orange", 1)

    print("Apple stock:", system.get_qty("apple"))
    print("Low items:", system.check_low_items())
    system.save_data()
    system.load_data()
    system.print_data()


if __name__ == "__main__":
    main()
