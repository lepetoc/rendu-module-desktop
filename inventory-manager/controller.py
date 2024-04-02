import sqlite3

class Controller():
    def __init__(self):
        self.conn = sqlite3.connect('inventory-manager.sqlite')
        self.cursor = self.conn.cursor()
        self.add_product(('Zuchini', 'A vegetable', 'Vegetable', 5.99))
        # print(self.get_products())
        
    def add_product(self, product):
        print(self.cursor.execute("INSERT INTO products (name, desc, category, price) VALUES (?, ?, ?, ?) RETURNING * ;", product))
        # self.cursor.execute("INSERT INTO stock (product_id, quantity, stock_threshold) VALUES (?, ?, ?, ?)", product)
        self.conn.commit()
        
    def add_supplier(self, supplier):
        self.cursor.execute("INSERT INTO suppliers (name, phone) VALUES (?, ?)", supplier)
        self.conn.commit()
    
    def add_sale(self, sale):
        self.cursor.execute("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", sale)
        self.conn.commit()