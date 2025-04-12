import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    'host': 'localhost',
    'database': 'bookstoredb',
    'user': 'root',
    'password': 'Agwanda@123'
}

def get_connection():
    """Establish and return a MySQL connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as err:
        print(f"Error: {err}")
        return None

def insert_data(query, data, description):
    """Generic function to insert data into a table."""
    conn = get_connection()
    if not conn:
        return
    
    with conn.cursor() as cursor:
        try:
            cursor.executemany(query, data)
            conn.commit()
            print(f"{cursor.rowcount} {description} inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conn.rollback()
        finally:
            conn.close()

# Insert functions
def insert_country(country_list):
    """Insert countries into the 'country' table."""
    query = "INSERT INTO country (country_name) VALUES (%s)"
    insert_data(query, country_list, "countries")

def insert_order_status(status_list):
    """Insert order statuses into the 'order_status' table."""
    query = "INSERT INTO order_status (status_name) VALUES (%s)"
    insert_data(query, status_list, "order statuses")

def insert_shipping_method(shipping_method_list):
    """Insert shipping methods into the 'shipping_method' table."""
    query = "INSERT INTO shipping_method (method_name, cost) VALUES (%s, %s)"
    insert_data(query, shipping_method_list, "shipping methods")

def insert_book_language(language_list):
    """Insert book languages into the 'book_language' table."""
    query = "INSERT INTO book_language (language_name) VALUES (%s)"
    insert_data(query, language_list, "languages")

def insert_publisher(publisher_list):
    """Insert publishers into the 'publisher' table."""
    query = "INSERT INTO publisher (name, country_id) VALUES (%s, %s)"
    insert_data(query, publisher_list, "publishers")

def insert_author(author_list):
    """Insert authors into the 'author' table."""
    query = "INSERT INTO author (first_name, last_name) VALUES (%s, %s)"
    insert_data(query, author_list, "authors")

def insert_book(book_list):
    """Insert books into the 'book' table."""
    query = "INSERT INTO book (title, isbn, language_id, publisher_id, price, quantity_in_stock) VALUES (%s, %s, %s, %s, %s, %s)"
    insert_data(query, book_list, "books")

def insert_book_author(book_author_list):
    """Insert book-author relationships into the 'book_author' table."""
    query = "INSERT INTO book_author (book_id, author_id) VALUES (%s, %s)"
    insert_data(query, book_author_list, "book-author relationships")

def insert_customer(customer_list):
    """Insert customers into the 'customer' table."""
    query = "INSERT INTO customer (first_name, last_name, email) VALUES (%s, %s, %s)"
    insert_data(query, customer_list, "customers")

def insert_address(address_list):
    """Insert addresses into the 'address' table."""
    query = "INSERT INTO address (street, city, postal_code, country_id) VALUES (%s, %s, %s, %s)"
    insert_data(query, address_list, "addresses")

def insert_address_status(status_list):
    """Insert address statuses into the 'address_status' table."""
    query = "INSERT INTO address_status (status_name) VALUES (%s)"
    insert_data(query, status_list, "address statuses")

def insert_customer_address(customer_address_list):
    """Insert customer addresses into the 'customer_address' table."""
    query = "INSERT INTO customer_address (customer_id, address_id, status_id) VALUES (%s, %s, %s)"
    insert_data(query, customer_address_list, "customer addresses")

def insert_cust_order(order_list):
    """Insert customer orders into the 'cust_order' table."""
    query = "INSERT INTO cust_order (customer_id, address_id, method_id, status_id, order_date) VALUES (%s, %s, %s, %s, %s)"
    insert_data(query, order_list, "customer orders")

def insert_order_line(order_line_list):
    """Insert order lines into the 'order_line' table."""
    query = "INSERT INTO order_line (order_id, book_id, quantity, price) VALUES (%s, %s, %s, %s)"
    insert_data(query, order_line_list, "order lines")

# Main Block to Insert Data
if __name__ == '__main__':
    # Insert countries, order statuses, shipping methods, languages
    countries = [
        ('Kenya',),
        ('South Africa',),
    ]
    insert_country(countries)

    order_status = [
        ('Pending',),
        ('Shipped',),
    ]
    insert_order_status(order_status)

    shipping_methods = [
        ('Standard Shipping', 5.99),
        ('Express Shipping', 15.99),
    ]
    insert_shipping_method(shipping_methods)

    book_languages = [
        ('English',),
        ('Spanish',),
    ]
    insert_book_language(book_languages)

    # Insert publishers
    publishers = [
        ('Penguin Books', 1),
        ('Bloomsbury Publishing', 2),
    ]
    insert_publisher(publishers)

    # Insert authors
    authors = [
        ('Agatha', 'Christie'),
        ('F. Scott', 'Fitzgerald'),
    ]
    insert_author(authors)

    # Insert books
    books = [
        ('Murder on the Orient Express', '978-0062073501', 1, 1, 14.99, 80),
        ('The Great Gatsby', '978-0743273565', 1, 2, 12.50, 100),
    ]
    insert_book(books)

    #  Insert book-author relationships
    book_authors = [
        (1, 1),  # Book 1 with Author 1
        (2, 2),  # Book 2 with Author 2
    ]
    insert_book_author(book_authors)

    # Step 6: Insert customers
    customers = [
        ('Angeline', 'Ivyne', 'ivyneangeline@gmail.com'),
        ('Abel', 'Sifuna', 'abelsifuna155@gmail.com'),
    ]
    insert_customer(customers)

    # Insert addresses
    addresses = [
        ('Kenya Road', 'Nairobi', '00100', 1),
        ('Long Street', 'Cape Town', '8001', 2),
    ]
    insert_address(addresses)

    # Step 8: Insert address statuses
    address_statuses = [
        ('Current',),
        ('Old',),
    ]
    insert_address_status(address_statuses)

    # Insert customer addresses
    customer_addresses = [
        (1, 1, 1),  # Customer 1 with Address 1, status "Current"
        (2, 2, 1),  # Customer 2 with Address 2, status "Current"
    ]
    insert_customer_address(customer_addresses)

    # Insert orders
    orders = [
        (1, 1, 1, 1, '2025-04-12'),
        (2, 2, 2, 2, '2025-04-13'),
    ]
    insert_cust_order(orders)

    # Insert order lines
    order_lines = [
        (1, 1, 2, 15.99),
        (1, 2, 1, 9.99),
        (2, 1, 1, 15.99),
        (2, 2, 1, 9.99),
    ]
    insert_order_line(order_lines)