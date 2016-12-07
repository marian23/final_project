from database import *
from peewee import *

db = SqliteDatabase('war_card_game')

class Base_model(Model):
    class Meta:
        database = db

class war_photo(Base_model):
    img_src = CharField(max_length=500, unique=True)
    suite = CharField(max_length=200)
    value = IntegerField( )



