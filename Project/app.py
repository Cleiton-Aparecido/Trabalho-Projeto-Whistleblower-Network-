import os
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from routes.index import AppRoutes
from flask.templating import render_template

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT')

database = MySQL(app)

@app.route('/register')
def register():
    return render_template('intro/register_form.html')

@app.route('/login')
def login():
    return render_template('intro/login_form.html')

@app.route('/password_reset')
def password_reset():
    return render_template('intro/reset_password_form.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'))