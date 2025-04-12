import mysql.connector
from mysql.connector import Error

def setup_roles_and_users():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Agwanda@123',
            database='bookstoredb'
        )
        cursor = connection.cursor()

        commands = [
            "CREATE ROLE IF NOT EXISTS 'admin_role';",
            "CREATE ROLE IF NOT EXISTS 'analyst_role';",
            "CREATE ROLE IF NOT EXISTS 'readonly_role';",

            "GRANT ALL PRIVILEGES ON bookstoredb.* TO 'admin_role';",
            "GRANT SELECT, INSERT, UPDATE ON bookstoredb.book TO 'analyst_role';",
            "GRANT SELECT ON bookstoredb.* TO 'readonly_role';",

            "CREATE USER IF NOT EXISTS 'admin_user'@'localhost' IDENTIFIED BY 'AdminPass123';",
            "CREATE USER IF NOT EXISTS 'analyst_user'@'localhost' IDENTIFIED BY 'AnalystPass123';",
            "CREATE USER IF NOT EXISTS 'readonly_user'@'localhost' IDENTIFIED BY 'ReadOnly123';",

            "GRANT 'admin_role' TO 'admin_user'@'localhost';",
            "GRANT 'analyst_role' TO 'analyst_user'@'localhost';",
            "GRANT 'readonly_role' TO 'readonly_user'@'localhost';",

            "SET DEFAULT ROLE 'admin_role' TO 'admin_user'@'localhost';",
            "SET DEFAULT ROLE 'analyst_role' TO 'analyst_user'@'localhost';",
            "SET DEFAULT ROLE 'readonly_role' TO 'readonly_user'@'localhost';"
        ]

        for cmd in commands:
            cursor.execute(cmd)
        
        connection.commit()
        print("Roles and users created successfully.")

    except Error as e:
        print("Error:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    setup_roles_and_users()