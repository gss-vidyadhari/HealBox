# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from login_authentication import handle_login_request
from register_authentication import handle_registration_request
from moto import get_random_quote


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        handle_registration_request(request)
        # Redirect to a different page after successful registration
        return redirect(url_for('login'))
    else:
        # If it's a GET request, render the registration template
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        authenticated = handle_login_request(request)

        if authenticated:
            # If login is successful, redirect to a different page
            return redirect(url_for('quote'))
        else:
            # If login fails, show an error message
            error = 'Invalid username or password'
            return render_template('login1.html', error=error)
    else:
        # If it's a GET request, render the login template
        return render_template('login1.html')


@app.route('/quote')
def quote():

    quote = get_random_quote()
    return render_template('quote.html', quote=quote)


if __name__ == '__main__':
    app.run()
