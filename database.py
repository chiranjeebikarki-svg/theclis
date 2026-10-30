import sqlite3


def init_db():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS inventory(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        quantity INTEGER NOT NULL,

        price REAL NOT NULL


        )

    ''')

    conn.commit()
    conn.close()

def add_item(name, quantity, price):
    if not name or quantity < 0 or price < 0:
        print("Error: Invalid item details.")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(
        '''
            INSERT INTO inventory("name, quantity, price")
            VALUES(?, ?, ?)
    ''', 
    
        (name, quantity, price),
        
    )

    conn.commit()
    conn.close()
    print(f"added '{name}' successfully")

def get_items():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    conn.close()

    print("n\-- current inventory ---")
    for row in items:
        print(f"ID: {row[0]} | Name: {row[1]} | Qty: {row[2]} | Price: ${row[3]:.2f}")

def update_item(item_id, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE inventory
        SET quantity = ?, price = ?
        WHERE id = ?
    ''', (quantity, price, item_id))

    conn.commit()
    conn.close()
    print(f"Updated item_id {item_id} successfully")

def delete_item(item_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    print(f"Deleted item_id {item_id} successfully.")


def main():
    init_db()
    print("Database and Table initialized successfully.")

    add_item("Wireless Mouse", 35, 15.50)
    get_items()
    
    # Pass valid arguments matching database IDs
    update_item(1, 40, 14.99)
    delete_item(1)


if __name__ == "__main__":
    main()



