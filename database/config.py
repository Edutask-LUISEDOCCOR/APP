from peewee import SqliteDatabase, PostgresqlDatabase, Model, AutoField, CharField, BooleanField, ForeignKeyField
from dotenv import load_dotenv
import os 

load_dotenv(".env.local")

if(os.getenv("environment") == "production"):
    DB_NAME = os.getenv('DB_NAME')
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    db = PostgresqlDatabase( 
        DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
else:
    db = SqliteDatabase("./database/database.db")

class User (Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

class Task (Model):
    id = AutoField()
    isDone = BooleanField(default=False)
    isPublic = BooleanField(default=False)
    title = CharField()
    content = CharField()
    user =  ForeignKeyField(User, backref="tasks")

    class Meta:
        database = db