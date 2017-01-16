import os
import sys
import time

PROGRAM_PATH = os.path.dirname(os.path.abspath(__file__))
# Add "common" directory to the Python's path
# TODO: Change it to os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# http://stackoverflow.com/a/11158224
COMMON_DIR = os.path.dirname(PROGRAM_PATH)
sys.path.insert(0, COMMON_DIR)

from common.models.reaction import Reaction
from common.utils.dir import make_sure_path_exists
from config import Config
from pychan import PyChan

from peewee import *


CONFIG_FILE_NAME = os.path.join(PROGRAM_PATH, 'config.ini')
IMGS_PATH = os.path.join(PROGRAM_PATH, 'imgs')


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


def create_tables():
  Reaction.create_table(True)


def main():
  connect_to_db()
  create_tables()

  pychan = PyChan()
  boards = pychan.get_boards()
  for board in boards:
    try:
      time.sleep(1.0)
      board_name = board['board']
      board_imgs_path = os.path.join(IMGS_PATH, board_name)
      make_sure_path_exists(board_imgs_path)
      threads = pychan.get_threads(board_name)
      for thread in threads:
        try:
          time.sleep(1.0)
          thread_number = thread['no']
          # TODO: Check images count
          posts = pychan.get_posts(board_name, thread_number)
          for post in posts:
            try:
              comment = post.get('com', '')
              if 'mfw' in comment or 'tfw' in comment:
                file_name = str(post.get('tim', '')) + post.get('ext', '')
                if not file_name:
                  continue
                time.sleep(1.0)
                img = pychan.get_image(board_name, file_name)
                file_path = os.path.join(board_imgs_path, file_name)
                # Save image to FS
                with open(file_path, 'wb') as f:
                  f.write(img)
                # Save image info to DB
                reaction = Reaction(
                  board_name=board_name,
                  file_name=file_name,
                  file_path=file_path,
                  comment=comment
                )
                reaction.save()
            except Exception as ex:
              print(ex)
        except Exception as ex:
          print(ex)
    except Exception as ex:
      print(ex)


if __name__ == '__main__':
  main()

