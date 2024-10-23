# add orders
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        santa_id = 6
        order_date = "2024-11-01"

        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"

        cursor.execute(query, (order_date, santa_id))
        conn.commit()
        print("Order added successfully for customer.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()

else:
    print("Couldn't find the database.")