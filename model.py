from peewee import *

db = SqliteDatabase('contacts.db')

class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    number = CharField()
    password = CharField()
    created_by = CharField()
    
    class Meta:
        database = db
        
db.connect()

db.create_tables([Contact])
