# add customer
from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        new_customer = ("Santa Claus", "santaworkshop@northpole.com", "0120250000", "1901-12-25")

        query = "INSERT INTO Customers (name, email, phone, birthday) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, new_customer)
        conn.commit()
        print("New customer added successfully.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()

else:
    print("Couldn't find the database.")