# update customers
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        updated_customer = ("122542069", 6)

        query = "UPDATE Customers SET phone = %s WHERE id = %s"

        cursor.execute(query, updated_customer)
        conn.commit()
        print("Customer details updated successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()

else:
    print("Couldn't find the database.")