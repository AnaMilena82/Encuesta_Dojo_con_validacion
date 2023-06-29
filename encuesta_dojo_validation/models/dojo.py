
from config.mysqlconnection import connectToMySQL
from flask import flash
from __init__ import BASE_DE_DATOS

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos;"
        dojos = []
        results = connectToMySQL(BASE_DE_DATOS).query_db(query)
        
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def new_dojo(cls, data ):
        query = "INSERT INTO dojos ( name , location, language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        return connectToMySQL(BASE_DE_DATOS).query_db( query, data )        

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # asumimos que esto es true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (dojo['location']) == "Seleccione...":
            flash("please select a location.")
            is_valid = False
        if (dojo['language']) == "Seleccione...":
            flash("please select a location.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid
    

