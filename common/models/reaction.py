from peewee import *


class Reaction(Model):
  board_name = CharField()
  file_name = CharField()
  file_path = CharField()  # TODO: Make it TextField?  # TODO: Make unique
  comment = TextField()

  class Meta:
    # peewee creates table names without 's' postfix, so let's do it manually
    db_table = 'reactions'

