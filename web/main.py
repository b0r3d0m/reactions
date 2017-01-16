import os
import sys

PROGRAM_PATH = os.path.dirname(os.path.abspath(__file__))
# Add "common" directory to the Python's path
# TODO: Change it to os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# http://stackoverflow.com/a/11158224
COMMON_DIR = os.path.dirname(PROGRAM_PATH)
sys.path.insert(0, COMMON_DIR)

from common.models.reaction import Reaction
from common.utils.url import get_mime_for_path, get_data_url_for_path
from common.utils.html import strip_tags, replace_brs
from config import Config

from peewee import *
from flask import Flask, render_template
app = Flask(__name__)

CONFIG_FILE_NAME = os.path.join(PROGRAM_PATH, 'config.ini')

config = Config()
config.load(CONFIG_FILE_NAME)

db = MySQLDatabase(
  config.db_schema,
  host=config.db_host,
  user=config.db_username,
  passwd=config.db_password
)
setattr(Reaction._meta, 'database', db)


def connect_to_db():
  db.connect()


@app.route('/')
def index():
  random_reactions = Reaction.select().order_by(fn.Rand()).limit(5)
  for reaction in random_reactions:
    reaction.mime_type = get_mime_for_path(reaction.file_path)
    reaction.data_url = get_data_url_for_path(reaction.file_path)
    reaction.comment_raw = strip_tags(replace_brs(reaction.comment, '. '))
  return render_template('index.html', reactions=random_reactions)


def main():
  connect_to_db()
  app.run()


if __name__ == '__main__':
  main()

