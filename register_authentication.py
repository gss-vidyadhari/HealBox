import mysql.connector

def create_user(username, password,email):
    # Establish a connection to the database
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Siricherry_2002',
        database='healbox'
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the query to fetch the user with the provided username
    query = "INSERT INTO newuser (username, password, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, email))

    # Commit the changes to the database
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    db.close()


def handle_registration_request(request):
    # Handle the registration request
    # Access the submitted form data from the request object
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Call the create_user function from register_authentication.py
    create_user(username, password, email)