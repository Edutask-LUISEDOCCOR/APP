from peewee import SqliteDatabase, Model, AutoField, CharField

db = SqliteDatabase("./database/database.db")

class User (Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db