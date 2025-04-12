import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    database="bookstoredb",
    user="root",  
    password="Agwanda@123"  # Add your password
)

# Create a cursor object
cursor = conn.cursor()

# Country Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS country (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL
)
""")

# Order Status
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_status (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(50) -- e.g. pending, shipped
)
""")

# Shipping Method Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shipping_method (
    method_id INT PRIMARY KEY AUTO_INCREMENT,
    method_name VARCHAR(50),
    cost DECIMAL(6,2)
)
""")

# Book Language Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book_language (
    language_id INT PRIMARY KEY AUTO_INCREMENT,
    language_name VARCHAR(50)
)
""")

# Publisher Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS publisher (
    publisher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
)
""")

# Author Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS author (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
)
""")

# Book Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    language_id INT,
    publisher_id INT,
    price DECIMAL(10,2),
    quantity_in_stock INT,
    FOREIGN KEY (language_id) REFERENCES book_language(language_id),
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
)
""")

# Book Author Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book_author (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id),
    FOREIGN KEY (author_id) REFERENCES author(author_id)
)
""")

# Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
)
""")

# Address Status Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS address_status (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(50) -- e.g. current, old
)
""")

# Address Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS address (
    address_id INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(100),
    city VARCHAR(50),
    postal_code VARCHAR(20),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
)
""")

# Customer Address Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_address (
    cust_addr_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    address_id INT,
    status_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (address_id) REFERENCES address(address_id),
    FOREIGN KEY (status_id) REFERENCES address_status(status_id)
)
""")

# Cust Order Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cust_order (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    address_id INT,
    method_id INT,
    status_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (address_id) REFERENCES address(address_id),
    FOREIGN KEY (method_id) REFERENCES shipping_method(method_id),
    FOREIGN KEY (status_id) REFERENCES order_status(status_id)
)
""")

# Order Line Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_line (
    order_line_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    book_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES cust_order(order_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
)
""")

# Order History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_history (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    status_id INT,
    changed_on DATETIME,
    FOREIGN KEY (order_id) REFERENCES cust_order(order_id),
    FOREIGN KEY (status_id) REFERENCES order_status(status_id)
)
""")

# Commit the changes
conn.commit()

print("Tables created successfully.")

# Close the connection
cursor.close()
conn.close()