import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'just-in-case-jskksk-hjjjbvy')

print(app.config['SECRET_KEY'])
db = SQLAlchemy(app)


from ecommerce import routes