from typing import Type
from database.config import User
from peewee import DoesNotExist

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
        try:
            data = self.user(username=username, password=password)
            data.save()
            return data
        except:
            return False



