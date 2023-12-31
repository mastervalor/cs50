from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

class Users:
    db = 'rideshare'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) <= 0 or len(user['last_name']) <= 0 or len(user['email']) <= 0 or len(user['password']) <= 0:
            is_valid = False
            flash('All fields required',"register")
            return is_valid
        if len(user['first_name']) < 2:
            flash('First Name must be at least 2 characters',"register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name must be at least 2 characters',"register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invald email address',"register")
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash('Password must have at least eight characters, at least one uppercase letter, one lowercase letter, one number and one special character',"register")
            is_valid = False
        if user['password_confirm'] != user['password']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid