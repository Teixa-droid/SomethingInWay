#Definitation of the schema of the DB
#This is a DB for managing information about clients, products and order in a store

#Create the DB
USE store_db;

#Create the kernel tables: zips, clients and products
CREATE TABLE IF NOT EXISTS zips(
	zip VARCHAR(6) NOT NULL,
    z_city VARCHAR(35) NOT NULL,
    z_state VARCHAR(35) NOT NULL,
    PRIMARY KEY(zip)
)ENGINE INNODB;

CREATE TABLE IF NOT EXISTS clients(
	id_client INT NOT NULL AUTO_INCREMENT,
    c_fname VARCHAR(35) NOT NULL,
    c_sname1 VARCHAR(35) NOT NULL,
    c_sname2 VARCHAR(35),
    c_street VARCHAR(35) NOT NULL,
    c_noext VARCHAR(7) NOT NULL,
    c_noint VARCHAR(7),
    c_col VARCHAR(35),
    c_zip VARCHAR(6),
    c_email VARCHAR(35),
    c_phone VARCHAR(13),
    PRIMARY KEY(id_client),
    CONSTRAINT fkzip_clients FOREIGN KEY(c_zip)
		REFERENCES zips(zip)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS products(
	id_product INT NOT NULL AUTO_INCREMENT,
    c_name VARCHAR(35) NOT NULL,
    c_brand VARCHAR(35) NOT NULL,
    c_descrip VARCHAR(250),
    c_price FLOAT NOT NULL,
    PRIMARY KEY(id_product)
)ENGINE = INNODB;

#Create the dependent tables: order and order details
CREATE TABLE IF NOT EXISTS orders(
	id_order INT NOT NULL AUTO_INCREMENT,
	id_client INT,
    o_status ENUM('PROCESSING', 'ACEPTED', 'SENT', 'RECEIVED') NOT NULL,
    o_date DATE NOT NULL, #Since MySql deals directly with dates
    o_date FLOAT NOT NULL,
    PRIMARY KEY(id_order),
    CONSTRAINT fkclient_orders FOREIGN KEY(id_client)
		REFERENCES clients(id_client)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS order_details(
	id_order INT NOT NULL,
	id_product INT NOT NULL,
    od_amount INT NOT NULL,
    od_total FLOAT NOT NULL,
    PRIMARY KEY(id_order, id_product),
    CONSTRAINT fkproduct_ods FOREIGN KEY(id_order)
		REFERENCES orders(id_order)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
    CONSTRAINT fkproduct_ods FOREIGN KEY(id_product)
		REFERENCES products(id_product)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)ENGINE = INNODB;

