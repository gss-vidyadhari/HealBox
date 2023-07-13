import mysql.connector

def authenticate_login(username, password):
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
    query = "SELECT * FROM newuser WHERE username = %s"
    cursor.execute(query, (username,))

    user = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Perform authentication logic
    # Check if the user exists and if the provided password matches
    if user and user[1] == password:
        return True
    else:
        return False

def handle_login_request(request):
    # Handle the login request
    # Access the submitted form data from the request object
    username = request.form['username']
    password = request.form['password']

    # Call the authenticate_login function from login_authentication.py
    authenticated = authenticate_login(username, password)

    return authenticated
