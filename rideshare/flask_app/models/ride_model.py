from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

class Rides:
    db = 'rideshare'
    def __init__ (self,data):
        self.id = data['id']
        self.destination = data['destination']
        self.pick_up = data['pick_up']
        self.date = data['date'].strftime('%b %d')
        self.details = data['details']
        self.rider_id = data['rider_id']
        self.rider_name = data['first_name']
        self.driver_id = data['driver_id']
        self.driver_name = data['first_name']

    @classmethod
    def get_all_ride_requests(cls):
        query = "SELECT * from rides join users on users.id = rides.rider_id where rides.driver_id is null"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_all_ride_booked(cls):
        query = "SELECT * from rides join users as riders on riders.id = rides.rider_id left join users as drivers on drivers.id = rides.driver_id where rides.driver_id is not null"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            thisuser = cls(row)
            thisuser.driver_name = row['drivers.first_name']
            users.append(thisuser)
        return users
    
    @classmethod
    def create_ride(cls,data):
        query = "INSERT Into rides(destination, pick_up, date, details, rider_id) values (%(destination)s, %(pick_up)s, %(date)s, %(details)s, %(rider_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete_ride(cls,data):
        query = "DELETE From rides where rides.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def driver_accpet(cls,data):
        query = "UPDATE rides set driver_id = %(driver_id)s where rides.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_one_ride(cls, data):
        query = "SELECT * from rides join users as riders on riders.id = rides.rider_id left join users as drivers on drivers.id = rides.driver_id where rides.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        thisuser = cls(results[0])
        thisuser.driver_name = results[0]['drivers.first_name']
        return thisuser
    
    @classmethod
    def cancel_driver(cls, data):
        query = "UPDATE rides set driver_id = null where rides.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update_ride(cls,data):
        query= "UPDATE rides set pick_up = %(pick_up)s, details = %(details)s where rides.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_create_ride(ride):
        is_valid = True
        if len(ride['destination']) <= 0 or len(ride['pick_up']) <= 0 or len(ride['date']) <= 0 or len(ride['details']) <= 0:
            is_valid = False
            flash('All fields are required', 'create')
            return is_valid
        if len(ride['pick_up']) <= 3:
            is_valid = False
            flash('Pick up must be at least 3 characters', 'create')
        if len(ride['details']) <= 10:
            is_valid = False
            flash('Details must be at least 3 characters', 'create')
        if len(ride['destination']) <= 3:
            is_valid = False
            flash('Destination must be at least 3 characters', 'create')
        return is_valid
    
    @staticmethod
    def validate_edit_ride(ride):
        is_valid = True
        if len(ride['pick_up']) <= 0 or len(ride['details']) <= 0:
            is_valid = False
            flash('All fields are required', 'edit')
            return is_valid
        if len(ride['pick_up']) <= 3:
            is_valid = False
            flash('Pick up must be at least 3 characters', 'edit')
        if len(ride['details']) <= 10:
            is_valid = False
            flash('Details must be at least 3 characters', 'edit')
        return is_valid