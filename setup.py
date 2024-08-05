#!/bin/bash

# Create the project directory
mkdir -p flask_app/{auth,models,static/css,static/js,templates}

# Create app.py
cat <<EOL > flask_app/app.py
from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from auth.signup import signup_bp
from auth.signin import signin_bp
from auth.reset_password import reset_password_bp

app.register_blueprint(signup_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(reset_password_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
EOL

# Create config.py
cat <<EOL > flask_app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'
EOL

# Create requirements.txt
cat <<EOL > flask_app/requirements.txt
Flask
EOL

# Create auth/__init__.py
touch flask_app/auth/__init__.py

# Create auth/signup.py
cat <<EOL > flask_app/auth/signup.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

signup_bp = Blueprint('signup', __name__)

# Dummy user data storage for demonstration purposes
users = {}

@signup_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
            return redirect(url_for('signup.register'))
        users[username] = password
        flash('Registration successful')
        return redirect(url_for('signin.login'))
    return render_template('register.html')
EOL

# Create auth/signin.py
cat <<EOL > flask_app/auth/signin.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

signin_bp = Blueprint('signin', __name__)

# Reference to the users dictionary in signup.py
from auth.signup import users

@signin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('signin.login'))
    return render_template('login.html')

@signin_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin.login'))
EOL

# Create auth/reset_password.py
cat <<EOL > flask_app/auth/reset_password.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

reset_password_bp = Blueprint('reset_password', __name__)

# Reference to the users dictionary in signup.py
from auth.signup import users

@reset_password_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        if username in users:
            users[username] = new_password
            flash('Password reset successful')
            return redirect(url_for('signin.login'))
        else:
            flash('Username not found')
            return redirect(url_for('reset_password.reset_password'))
    return render_template('reset_password.html')
EOL

# Create models/user.py
cat <<EOL > flask_app/models/user.py
# Dummy user data model for demonstration purposes
# This file can be extended with actual database models later
EOL

# Create templates/base.html
cat <<EOL > flask_app/templates/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Flask App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('home') }}">Home</a></li>
                {% if 'username' in session %}
                    <li><a href="{{ url_for('signin.logout') }}">Logout</a></li>
                {% else %}
                    <li><a href="{{ url_for('signin.login') }}">Login</a></li>
                    <li><a href="{{ url_for('signup.register') }}">Register</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>
    <main>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </main>
</body>
</html>
EOL

# Create templates/home.html
cat <<EOL > flask_app/templates/home.html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Welcome to the Flask App</h2>
    {% if 'username' in session %}
        <p>Hello, {{ session['username'] }}!</p>
    {% else %}
        <p>Please log in or register.</p>
    {% endif %}
{% endblock %}
EOL

# Create templates/login.html
cat <<EOL > flask_app/templates/login.html
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block content %}
    <h2>Login</h2>
    <form method="post" action="{{ url_for('signin.login') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
{% endblock %}
EOL

# Create templates/register.html
cat <<EOL > flask_app/templates/register.html
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block content %}
    <h2>Register</h2>
    <form method="post" action="{{ url_for('signup.register') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
{% endblock %}
EOL

# Create templates/reset_password.html
cat <<EOL > flask_app/templates/reset_password.html
{% extends "base.html" %}

{% block title %}Reset Password{% endblock %}

{% block content %}
    <h2>Reset Password</h2>
    <form method="post" action="{{ url_for('reset_password.reset_password') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="new_password">New Password:</label>
        <input type="password" id="new_password" name="new_password" required><br><br>
        <input type="submit" value="Reset Password">
    </form>
{% endblock %}
EOL

# Create static/css/styles.css
cat <<EOL > flask_app/static/css/styles.css
body {
    font-family: Arial, sans-serif;
}

header {
    background: #333;
    color: #fff;
    padding: 1em 0;
}

header nav ul {
    list-style: none;
    padding: 0;
}

header nav ul li {
    display: inline;
    margin-right: 10px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

main {
    padding: 2em;
}
EOL

# Create static/js/scripts.js
cat <<EOL > flask_app/static/js/scripts.js
// Placeholder for future JavaScript code
EOL

# Print completion message
echo "Flask app structure created successfully."
