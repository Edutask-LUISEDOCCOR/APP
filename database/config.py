from peewee import SqliteDatabase, Model, AutoField, CharField, BooleanField, ForeignKeyField

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