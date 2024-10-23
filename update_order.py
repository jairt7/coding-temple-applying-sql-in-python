# update orders
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        customer_id = 6
        order_id = 2
        new_order_date = "2024-12-01"

        query = "UPDATE Orders SET date = %s WHERE id = %s AND customer_id = %s"

        cursor.execute(query, (new_order_date, order_id, customer_id))
        conn.commit()
        print("Order updated successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        conn.close()
        
else:
    print("Couldn't find the database.")