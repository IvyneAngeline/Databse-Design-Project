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

def execute_query(query):
    """Execute a query and return the results."""
    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def test_retrieve_data():
    """Test querying and analyzing data."""
    # Get all books and their details
    print("All Books:")
    query = "SELECT * FROM book"
    books = execute_query(query)
    for book in books:
        print(book)
    
    # Get all customers and their orders
    print("\nAll Customers and Their Orders:")
    query = """SELECT c.first_name, c.last_name, co.order_id, co.order_date 
               FROM customer c
               JOIN cust_order co ON c.customer_id = co.customer_id"""
    customers_orders = execute_query(query)
    for record in customers_orders:
        print(record)
    
    # Get the total number of books in stock
    print("\nTotal Books in Stock:")
    query = "SELECT SUM(quantity_in_stock) FROM book"
    total_books = execute_query(query)
    print(total_books[0][0])

    # Get the most expensive book
    print("\nMost Expensive Book:")
    query = "SELECT title, price FROM book ORDER BY price DESC LIMIT 1"
    most_expensive_book = execute_query(query)
    print(most_expensive_book[0])
    
    # Get total orders by order status
    print("\nTotal Orders by Status:")
    query = """SELECT os.status_name, COUNT(co.order_id)
               FROM cust_order co
               JOIN order_status os ON co.status_id = os.status_id
               GROUP BY os.status_name"""
    orders_by_status = execute_query(query)
    for status in orders_by_status:
        print(status)

if __name__ == '__main__':
    test_retrieve_data()