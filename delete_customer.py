# delete customers
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        customer_to_remove = (6, )

        query_check = "Select * FROM Orders WHERE customer_id = %s"
        cursor.execute(query_check, customer_to_remove)
        orders = cursor.fetchall()

        if orders:
            print("Cannot delete customer: they have associated orders.")

        else:
            query = "Delete FROM Customers WHERE id = %s"

            cursor.execute(query, customer_to_remove)
            conn.commit()
            print("Customer removed successfully.")


    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
else:
    print("Couldn't find the database.")