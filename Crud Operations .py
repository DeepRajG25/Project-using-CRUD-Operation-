import mysql.connector

# Function to establish a connection to the database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Update with your MySQL user
        password="123456",  # Update with your MySQL password
        database="UserDB"  # Update with your MySQL database
    )

# Function to close the connection
def close_connection(conn):
    conn.close()

# Function to create the Users table
def create_users_table():
    connection = create_connection()  # Use the correct function name
    cursor = connection.cursor()

    # SQL query to create the Users table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Users (
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(50) NOT NULL,
        Second_Name VARCHAR(50) NOT NULL,
        Full_Name VARCHAR(50) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Phone_No VARCHAR(15),
        City VARCHAR(50)
    );
    """

    # Execute the SQL query
    cursor.execute(create_table_query)

    # Commit the transaction
    connection.commit()

    print("Users table created successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Function to create a new user (INSERT operation)
def create_user(first_name, second_name, full_name, phone_no, email, city):
    connection = create_connection()  # Use the correct function name
    cursor = connection.cursor()

    # SQL query to insert a new user
    query = "INSERT INTO Users (First_Name, Second_Name, Full_Name, Phone_No, Email, City) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (first_name, second_name, full_name, phone_no, email, city)

    # Execute the query and commit the transaction
    cursor.execute(query, values)
    connection.commit()

    print(f"User {first_name} {second_name} added successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Main function
if __name__ == "__main__":
    # Create the Users table
    create_users_table()

     # Collect input from the command line
    first_name = input("Enter First Name: ")
    second_name = input("Enter Second Name: ")
    full_name = f"{first_name} {second_name}"  # Automatically generate full name
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")

    # Call the function to add the user to the database
    create_user(first_name, second_name, full_name, phone_no, email, city)
    
    # Example of adding a user
    # create_user('John', 'Doe', 'John Doe', '1234567890', 'john.doe@example.com', 'New York')
