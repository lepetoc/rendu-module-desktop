import sqlite3

class Model():
    def __init__(self):
        self.conn = sqlite3.connect('inventory-manager.sqlite')
        self.cursor = self.conn.cursor()
        # self.add_product(('Zuchini', 'A vegetable', 'Vegetable', 5.99))
        # print(self.get_products())
        self.get_stock()
        
    def add_product(self, product):
        self.cursor.execute("INSERT INTO products (name, desc, category, price) VALUES (?, ?, ?, ?);", product)
        self.cursor.execute("INSERT INTO stock (product_id, quantity, stock_threshold) VALUES (?, ?, ?)", (self.cursor.lastrowid, 0, 10))
        self.conn.commit()
        
    def add_supplier(self, supplier):
        self.cursor.execute("INSERT INTO suppliers (supplier_name, contact_info) VALUES (?, ?)", supplier)
        self.conn.commit()
    
    def add_sale(self, sale):
        self.cursor.execute("INSERT INTO sales (product_id, quantity, sale_date) VALUES (?, ?, ?)", sale)
        self.cursor.execute("UPDATE stock SET quantity = quantity - ? WHERE product_id = ?", (sale[1], sale[0]))
        self.conn.commit()
    
    def add_purchase(self, purchase):
        self.cursor.execute("INSERT INTO purchases (supplier_id, product_id, quantity, purchase_date) VALUES (?, ?, ?, ?);", purchase)
        self.cursor.execute("UPDATE stock SET quantity = quantity + ? WHERE product_id = ?", (purchase[2], purchase[1]))
        self.conn.commit()

    def get_stock(self):
        self.cursor.execute("""
        SELECT products.name, stock.quantity, stock.stock_threshold
        FROM products
        JOIN stock ON products.id = stock.product_id
        """)
        rows = self.cursor.fetchall()
        return rows
    
    def get_history(self):
        self.cursor.execute("""
        SELECT 
        'Purchase' AS transaction_type,
        suppliers.supplier_name AS supplier_name,
        products.name AS product_name,
        purchases.quantity AS quantity,
        purchases.purchase_date AS transaction_date
        FROM 
        purchases
        INNER JOIN suppliers ON purchases.supplier_id = suppliers.id
        INNER JOIN products ON purchases.product_id = products.id

        UNION

        SELECT 
        'Sale' AS transaction_type,
        NULL AS supplier_name,
        products.name AS product_name,
        sales.quantity AS quantity,
        sales.sale_date AS transaction_date
        FROM 
        sales
        INNER JOIN products ON sales.product_id = products.id
        """)
        rows = self.cursor.fetchall()
        return rows