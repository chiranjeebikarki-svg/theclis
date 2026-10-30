# SQLite Inventory Management System

A lightweight, secure command-line inventory management system built with Python and SQLite.

## Features
* **SQL Injection Prevention:** Uses parameterized queries (`?` placeholders) for all data mutations.
* **Full CRUD Lifecycle:** Create, Read, Update, and Delete items.
* **CLI Integration:** Powered by Python's `argparse` module.

## Usage
Add an item:
```bash
python inventory.py add --name "Item Name" --qty 10 --price 19.99