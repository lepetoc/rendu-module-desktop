INSERT INTO suppliers (supplier_name, contact_info) VALUES ('Example Supplier', 'example@supplier.com');
INSERT INTO products (name, desc, category, price) VALUES ('Example Product', 'An example product description', 'Example Category', 19.99);
INSERT INTO purchases (supplier_id, product_id, quantity, purchase_date) VALUES (1, 1, 100, strftime('%s','now'));
INSERT INTO stock (product_id, quantity, stock_threshold) VALUES (1, 100, 10);
INSERT INTO sales (product_id, quantity, sale_date) VALUES (1, 2, '2024-03-19');
