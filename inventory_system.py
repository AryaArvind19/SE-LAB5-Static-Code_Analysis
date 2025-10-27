"""Inventory management system for tracking and updating stock data."""

import json
from datetime import datetime
import ast

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Remove a specified quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock")

def get_qty(item):
    """Return the quantity of a given item in stock."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)

def save_data(file="inventory.json"):
    """Save current stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)

def print_data():
    """Display all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    """Return a list of items with stock below the given threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """Main function to test inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("mango", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    ast.literal_eval("('safe eval used')")

if __name__ == "__main__":
    main()
