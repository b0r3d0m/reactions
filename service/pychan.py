import requests


# TODO: Use HTTPS
class PyChan:
  def __init__(self):
    pass

  def get_boards(self):
    r = requests.get('http://a.4cdn.org/boards.json')
    return r.json()['boards']

  def get_threads(self, board_name):
    r = requests.get('http://a.4cdn.org/{board}/catalog.json'.format(board=board_name))
    threads = []
    pages = r.json()
    for page in pages:
      threads = threads + page['threads']
    return threads

  def get_posts(self, board_name, thread_num):
    r = requests.get('http://a.4cdn.org/{board}/thread/{threadnumber}.json'.format(board=board_name, threadnumber=thread_num))
    return r.json()['posts']

  def get_image(self, board_name, file_name):
    r = requests.get('http://i.4cdn.org/{board}/{filename}'.format(board=board_name, filename=file_name))
    return r.content

