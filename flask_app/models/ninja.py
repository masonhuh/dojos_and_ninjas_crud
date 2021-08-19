from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        return results

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        return results