import base64
from mimetypes import MimeTypes
import urllib


def get_mime_for_path(path):
  url = urllib.pathname2url(path)
  mime = MimeTypes()
  mime_type = mime.guess_type(url)
  return mime_type[0]
  if mime_type[0] == 'video/x-webm':
    return 'video/webm'
  else:
    return mime_type[0]


def get_data_url_for_path(path):
  with open(path, 'rb') as f:
    return 'data:{};base64,{}'.format(get_mime_for_path(path), base64.b64encode(f.read()))

