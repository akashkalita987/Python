import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akash@4918*"
    )

    if connection.is_connected():
        print("connected successfully")

        cursor = connection.cursor()

        cursor.execute("use python_demo;")
        print("database is ready to use\n")

        # 1. Execute the command
        cursor.execute("show tables;")
        
        # 2. Fetch all rows returned by the query
        tables = cursor.fetchall()
        
        print("--- Tables in python_demo ---")
        # 3. Loop through and print each table name
        for table in tables:
            print(table[0])  # table[0] gets the string out of the tuple
            
except mysql.connector.Error as error:
    print(f"there is error: {error}")
finally:
    # Always clean up and close connections
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nMySQL connection closed safely.")