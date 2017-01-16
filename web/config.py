import ConfigParser


class Config:
  def load(self, filename):
    config = ConfigParser.SafeConfigParser()
    config.read(filename)

    self.host = config.get('general', 'host')
    self.port = int(config.get('general', 'port'))

    self.db_schema = config.get('db', 'schema')
    self.db_host = config.get('db', 'host')
    self.db_username = config.get('db', 'username')
    self.db_password = config.get('db', 'password')

