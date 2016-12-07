import sqlite3
from peewee import *
import datetime

from peewee_model import war_photo

db = SqliteDatabase('war_card_game')

def set_up_data():
          db.connect()
          db.create_tables([war_photo], safe=True)
    #
def insert_card(card_data):
    try:
        new_card = war_photo.create(img_src=card_data.img_src, suite= card_data.suite, value=card_data.value)
        new_card.save()

    except IntegrityError:
        print("the card is already in database")



# conn = sqlite3.connect('databsae.db')
# print ("Opened database successfully")
#
# conn.execute('CREATE TABLE war ()')
# print ("Table created successfully")
# conn.close()
#value, suite, image