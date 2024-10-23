# fetching orders from a certain customer
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        query = """
        SELECT o.id AS OrderID, o.date AS OrderDate, c.id AS CustomerID, c.name, c.email
        FROM Customers c, Orders o
        WHERE c.id = o.customer_id AND c.name LIKE 'Santa%'
        """

        cursor.execute(query)

        for order in cursor.fetchall():
            print(order)
    
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        conn.close()
        
else:
    print("Couldn't find the database.")