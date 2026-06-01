import mysql.connector

try:
    # 1. Connect to the local MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="....."  # <-- Change this!
    )

    if connection.is_connected():
        print("Connected successfully to MySQL!")
        
        # 2. Create a cursor object
        cursor = connection.cursor()
        
        # 3. Create a brand new database for testing
        cursor.execute("CREATE DATABASE IF NOT EXISTS python_demo;")
        print("Database 'python_demo' is ready.")
        
        # 4. Switch to the new database
        cursor.execute("USE python_demo;")
        
        # 5. Create a table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100)
            );
        """)
        print("Table 'users' created successfully.")

        cursor.execute(
            """insert into users(name,email) values("akash","akash@gmail.com");"""
        )
        print("data inserted successfully")

        cursor.execute(
            "select * from users;"
        )
        for row in cursor:
            print(row)
except mysql.connector.Error as error:
    print(f"Something went wrong: {error}")

finally:
    # 6. Always clean up and close connections
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed safely.")