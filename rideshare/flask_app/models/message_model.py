from flask_app.config.mysqlconnection import connectToMySQL

class Messages:
    db = 'rideshare'
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.ride_id = data['ride_id']
        self.user_id = data['user_id']
        self.user_name = data['first_name']

    @classmethod
    def get_all_messages(cls,data):
        query = "SELECT * from messages join users on users.id = messages.user_id join rides on rides.id = messages.ride_id where rides.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        messages = []
        for row in results:
            messages.append(cls(row))
        return messages
    
    @classmethod
    def create_message(cls, data):
        query = "INSERT into messages(content, ride_id, user_id) values (%(content)s, %(ride_id)s, %(user_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)