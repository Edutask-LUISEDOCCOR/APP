from typing import Type
from database.config import User
from peewee import DoesNotExist
from lib.bcrypt import hash_password

class UserModel():
    def __init__(self, User: Type[User]) -> None:
        self.user = User

    def getByUsername(self, username):
        try:
            data = self.user.get(User.username == username)
            return data 
        except DoesNotExist:
            return False
        
    def getById(self, id):
        try:
            data = self.user.get(User.id == id)
            return data 
        except DoesNotExist:
            return False
    
    def create(self, username, password):
        #try:
            hashPassword = hash_password(password)
            data = self.user(username=username, password=hashPassword)
            data.save()
            return data
        #except :
            return False



