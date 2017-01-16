from HTMLParser import HTMLParser
import re


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def replace_brs(s, repl):
  return re.sub(r'\s*<br.*?>\s*', repl, s, flags=re.IGNORECASE)

