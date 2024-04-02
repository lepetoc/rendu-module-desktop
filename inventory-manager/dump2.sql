CREATE TABLE  suppliers (
     id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     supplier_name  TEXT NOT NULL,
     contact_info  TEXT NOT NULL
);
CREATE TABLE  purchases (
     id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     supplier_id  INTEGER NOT NULL,
     product_id  INTEGER NOT NULL,
     quantity  BIGINT NOT NULL,
     purchase_date  BIGINT NOT NULL,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
CREATE TABLE sales (
     id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     product_id  INTEGER NOT NULL,
     quantity  BIGINT NOT NULL,
     sale_date  DATE NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(id)
);
CREATE TABLE stock (
     id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     product_id  INTEGER NOT NULL,
     quantity  BIGINT NOT NULL,
     stock_threshold  BIGINT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES  products(id)
);
CREATE TABLE products (
     id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name  TEXT NOT NULL,
     desc  TEXT NOT NULL,
     category  TEXT NOT NULL,
     price  DOUBLE(8, 2) NOT NULL
);
-- ALTER TABLE
--      purchases  ADD CONSTRAINT  purchases_supplier_id_foreign  FOREIGN KEY( supplier_id ) REFERENCES  suppliers ( id );
-- ALTER TABLE
--      sales  ADD CONSTRAINT  sales_product_id_foreign  FOREIGN KEY( product_id ) REFERENCES  products ( id );
-- ALTER TABLE
--      purchases  ADD CONSTRAINT  purchases_product_id_foreign  FOREIGN KEY( product_id ) REFERENCES  products ( id );
-- ALTER TABLE
--      stock  ADD CONSTRAINT  stock_product_id_foreign  FOREIGN KEY( product_id ) REFERENCES  products ( id );